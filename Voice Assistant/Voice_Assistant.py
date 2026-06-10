import pygame
import time
import speech_recognition as sr
import pyttsx3
import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from transformers import pipeline
import subprocess

def identify_person():
    try:
        result = subprocess.run(
            ["your_venv_path/Scripts/python", "your_script_path/script.py"],
            capture_output=True, text=True
        )
        print("Output from script.py:", result.stdout)
        if result.returncode != 0:
            print("Error running script:", result.stderr)
            return "Sorry, there was an issue identifying the person."
        return "Person identification complete."
    except Exception as e:
        print(f"Error running identification script: {e}")
        return "Sorry, something went wrong with person identification."

def identify_currency():
    try:
        # Use the full path to the Python executable in your environment
        python_executable = r"your_venv_path\Scripts\python.exe"
        script_path = r"your_script_path/detect.py"
        
        # Run the currency detection script using the correct environment
        result = subprocess.run(
            [python_executable, script_path],
            capture_output=True, text=True, shell=True
        )
        print("Output from detect.py:", result.stdout)
        if result.returncode != 0:
            print("Error running currency detection script:", result.stderr)
            return "Sorry, there was an issue identifying the currency."
        return "Currency identification complete."
    except Exception as e:
        print(f"Error running currency detection script: {e}")
        return "Sorry, something went wrong with currency identification."



pygame.mixer.init()

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def load_jokes(file_path):
    with open(file_path, "r") as file:
        jokes = file.read().splitlines()
    return jokes

def load_context(file_path):
    with open(file_path, "r") as file:
        context = file.read()
    return context

jokes = load_jokes("jokes_file.txt")
context = load_context("context_file.txt")
current_joke_index = 0

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=10) 
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-US")
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            speak("Sorry, I did not hear anything. Please try again.")
            return None
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, something went wrong.")
            return None

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%A, %B %d, %Y")

def get_location():
    return "Locality, District, State"

def get_weather():
    return "The weather is sunny with a temperature of 25°C."

def get_timezone():
    try:
        location = get_location()
        geolocator = Nominatim(user_agent="voice_assistant")
        location_data = geolocator.geocode(location)
        tf = TimezoneFinder()
        timezone = tf.timezone_at(lat=location_data.latitude, lng=location_data.longitude)
        return timezone
    except Exception as e:
        print(f"Error fetching timezone: {e}")
        return "unknown timezone"

def get_answer(question):
    try:
        result = qa_pipeline(question=question, context=context)
        answer = result['answer']
        return answer
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't process your request."

def tell_joke():
    global current_joke_index
    if current_joke_index < len(jokes):
        joke = jokes[current_joke_index]
        current_joke_index += 1  
        return joke
    else:
        return "I'm out of jokes for now. Ask me again later!"

def play_music():
    try:
        music_file = "Audio_file"  
        print(f"Loading music file: {music_file}")
        pygame.mixer.music.load(music_file)
        print("Playing music...")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            stop_query = listen()
            if stop_query and ("stop music" in stop_query.lower() or "stop song" in stop_query.lower()):
                pygame.mixer.music.stop()
                print("Music stopped by user.")
                return "Music stopped."
            time.sleep(1)

        print("Music finished playing.")
        return "Playing music..."
    except Exception as e:
        print(f"Error playing music: {e}")
        return "Sorry, I couldn't play the music."

def stop_music():
    try:
        pygame.mixer.music.stop()
        return "Music stopped."
    except Exception as e:
        print(f"Error stopping music: {e}")
        return "Sorry, I couldn't stop the music."

def handle_command(query):
    query = query.lower()
    if "time" in query:
        speak(f"The current time is {get_time()}.")
    elif "date" in query:
        speak(f"Today's date is {get_date()}.")
    elif "location" in query:
        speak(f"You are currently in {get_location()}.")
    elif "weather" in query:
        speak(get_weather())
    elif "timezone" in query:
        speak(f"Your current timezone is {get_timezone()}.")
    elif "joke" in query or "tell me a joke" in query:
        speak(tell_joke())
    elif "play music" in query or "play song" in query:
        speak(play_music())
    elif "stop music" in query or "stop song" in query:
        speak(stop_music())
    elif "identify the person" in query:
        speak(identify_person())
    elif "identify the currency" in query:
        speak(identify_currency())
    elif "text to speech" in query:
        try:
            result = subprocess.run(
                ["your_venv_path/Scripts/python", "your_script_path/txt.py"],
                capture_output=True, text=True
            )
            print("Output from txt.py:", result.stdout)
            if result.returncode != 0:
                print("Error running txt.py:", result.stderr)
                speak("Sorry, there was an issue with text-to-speech.")
            else:
                speak("Text-to-speech conversion completed.")
        except Exception as e:
            print(f"Error running text-to-speech script: {e}")
            speak("Sorry, something went wrong with text-to-speech.")
    elif "exit" in query or "done" in query:
        speak("Goodbye!")
        return False
    else:
        speak("Let me think about that...")
        answer = get_answer(query)
        speak(answer)
    return True

def main():
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        query = listen()
        if query:
            if not handle_command(query):
                break

if __name__ == "__main__":
    main()

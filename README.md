![GuideMate Banner](GuideMate.png)
# GuideMate - Helping Hand for Visually Impaired Individuals

An AI-powered voice assistant designed to assist visually impaired individuals
with essential daily tasks using face recognition, currency detection, and
voice commands.

Built as a Mini Project B.Tech at Ilahia College of Engineering and
Technology, under APJ Abdul Kalam Technological University, Kerala.

---

## Project Structure

```

GuideMate/
│
├── Currency-Detection/
│   ├── Currency_Detection.py
│   ├── Image_Annotator.py
│   ├── Label_Generator.py
│   └── Label_Verifier.py
│
├── Face-Recognition/
│   ├── Face_Data_Collection.py
│   ├── Face_Encoder.py
│   └── Face_Recognizer.py
│
├── Voice-Assistant/
│   └── Voice_Assistant.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE
```
---

## How It Works

**Currency Detection**
- YOLOv8 model trained on Indian currency notes
- Detects currency denomination in real-time using webcam
- Announces the detected currency via text-to-speech

**Face Recognition**
- Collects face images using webcam
- Encodes and stores known faces using dlib
- Identifies and announces the person's name in real-time

**Voice Assistant**
- Listens to voice commands via microphone
- Responds to commands like time, date, jokes, music and more
- Uses DistilBERT AI model for answering general questions
- Triggers currency detection and face recognition on voice command

---

## Setup Instructions

### Python App
1. Clone this repository

2. Install dependencies:
```
pip install -r requirements.txt
```

3. For Face Recognition setup, run in order:
```
python Face_Data_Collection.py
python Face_Encoder.py
```

4. Download the following dlib model files and place them in the Face-Recognition folder:
- shape_predictor_68_face_landmarks.dat
- dlib_face_recognition_resnet_model_v1.dat

5. For Currency Detection setup, run in order:
```
python Image_Annotator.py
python Label_Generator.py
python Label_Verifier.py
```

6. Train your YOLOv8 model and place the trained model file in the Currency-Detection folder

7. Update the following in Voice_Assistant.py:
- your_venv_path — path to your virtual environment
- your_script_path — path to your scripts

8. Add your own files:
- jokes.txt — one joke per line
- context.txt — text for AI question answering
- Audio file — your preferred audio file for music

9. Run the assistant:
```
python Voice_Assistant.py
```

---

## Voice Commands

| You Say | What Happens |
|---|---|
| "What time is it?" | Tells the current time |
| "What is the date?" | Tells today's date |
| "What is the weather?" | Tells the weather |
| "Tell me a joke" | Tells a joke |
| "Play music" | Plays audio file |
| "Stop music" | Stops the audio |
| "Identify the person" | Runs face recognition |
| "Identify the currency" | Runs currency detection |
| "Text to speech" | Reads a document aloud |
| "Exit" | Closes the assistant |

---

## Hardware Required
- Webcam
- Microphone
- Speaker

---

## Tech Stack
- **AI Models:** YOLOv8, DistilBERT, dlib
- **Voice:** SpeechRecognition, pyttsx3
- **Computer Vision:** OpenCV, face_recognition
- **Frontend:** Python
- **Data:** CSV files, numpy

---

## Author
Althaf Ameen Haneefa
B.Tech — Artificial Intelligence and Data Science
Ilahia College of Engineering and Technology, Muvattupuzha
2025

---

## License
This project is licensed under the MIT License.

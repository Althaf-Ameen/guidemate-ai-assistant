import cv2
import torch
import pyttsx3
from ultralytics import YOLO  # Import YOLOv8

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

# Load the trained YOLOv8 model
model = YOLO('your_model_path')  # Update path to your trained weights
print(model.names)

# Confidence threshold
confidence_threshold = 0.8  # Adjust as needed

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

detected = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Detect currency using YOLOv8
    results = model(frame)  # Inference with YOLOv8

    # Process the results
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            confidence = box.conf[0].item()  # Confidence score
            class_id = int(box.cls[0].item())  # Class ID
            label = model.names[class_id]  # Get class name

            # Check if confidence is above threshold
            if confidence >= confidence_threshold:
                # Print the detected label and confidence
                print(f"Detected: {label} with confidence: {confidence:.2f}")

                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{label} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                # Voice announcement
                engine.say(f"Detected {label}")
                engine.runAndWait()

                # Set detected to True to exit after one detection
                detected = True
                break

        if detected:
            break

    # Display the frame
    cv2.imshow("Currency Detection", frame)

    # Exit after detecting one currency
    if detected:
        break

    # Press 'q' to quit manually
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

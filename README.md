# Face Recognition Attendance System

## Overview
This is a Python script that implements a face recognition-based attendance system using the K-Nearest Neighbors (KNN) algorithm. The system captures video from a webcam, detects faces in real-time, recognizes the faces using a pre-trained KNN model, and records attendance with timestamps in a CSV file.

## Prerequisites
- Python 3.x
- OpenCV (`cv2`)
- scikit-learn (`sklearn`)
- pywin32 (for text-to-speech, optional)

## Setup

1. **Install the required libraries:**
   ```bash
   pip install opencv-python scikit-learn pywin32
Ensure the following files are present in the specified directories:

haarcascade_frontalface_default.xml in the 'data' directory.
names.pkl and faces_data.pkl in the 'data' directory.
background.png for overlaying the webcam feed.
Run the script:

bash
Copy code
python face_recognition_attendance.py
##Functionality
The system uses the Haar Cascade classifier for face detection.
Trained KNN model (faces_data.pkl) and labels (names.pkl) are loaded from the 'data' directory.
Detected faces are resized and passed through the KNN model for recognition.
Real-time video feed is displayed with rectangles around detected faces and their names.
Press 'o' to mark attendance. The system will speak "Attendance Taken" and record the attendance in a CSV file with date and time stamps in the 'Attendance' directory.
Press 'q' to exit the application.
##Note
Ensure that the face recognition model (faces_data.pkl) and labels (names.pkl) are pre-trained before running the script.
The attendance data is stored in CSV files in the 'Attendance' directory.
##Credits
This project uses OpenCV for face detection and image processing.
The face recognition model is implemented using scikit-learn's KNeighborsClassifier.
Text-to-speech functionality is achieved using the pywin32 library.

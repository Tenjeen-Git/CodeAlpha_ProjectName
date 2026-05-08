# Object Detection and Tracking System
## Project Overview

This project performs real-time object detection and tracking using a webcam or video file. It uses the YOLOv8 pre-trained model for detecting objects and ByteTrack for assigning unique tracking IDs to detected objects.

The system:
- Captures video from webcam or video file
- Detects objects in each frame
- Draws bounding boxes around detected objects
- Tracks moving objects using tracking IDs
- Displays live output in real time

# Technologies Used

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- ByteTrack


# Project Structure

```txt
object_detection_tracking/
│
├── main.py
├── requirements.txt
├── README.md
└── videos/
    └── sample.mp4
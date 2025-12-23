# Real-Time Face Detection using Haar Cascade and OpenCV

## Project Overview
This project implements **real-time face detection** using the **Haar Cascade classifier** provided by OpenCV. The system captures live video from a webcam, processes each frame, detects human faces, and highlights them with bounding boxes in real time.

The project demonstrates a classic and widely used computer vision technique for object detection without deep learning.

---

## Objectives
- Capture live video stream using a webcam
- Detect human faces in real time
- Apply Haar Cascade classifiers for object detection
- Draw bounding boxes around detected faces
- Understand the working of traditional face detection methods

---

## Technologies Used
- Python 3
- OpenCV (cv2)

---

## Methodology

### 1. Video Capture
- Webcam initialized using OpenCV’s `VideoCapture`
- Frames are continuously read until the program is terminated

---

### 2. Frame Preprocessing
- Frames are flipped horizontally for mirror-like display
- Resized to a fixed resolution (500 × 500)
- Converted from BGR to Grayscale for faster and more effective detection

---

### 3. Face Detection using Haar Cascade
- Pre-trained Haar Cascade XML file used:
  - `haarcascade_frontalface_default.xml`
- The classifier scans the grayscale image at multiple scales
- Parameters used:
  - Scale Factor: 1.2
  - Minimum Neighbors: 4

---

### 4. Bounding Box Visualization
- Rectangles drawn around detected faces
- Green bounding boxes indicate detected face regions

---

### 5. Real-Time Display
- Annotated video feed displayed in a window
- Program exits cleanly when the **'p'** key is pressed

---

## Key Concepts Demonstrated
- Haar feature-based cascade classifiers
- Sliding window detection
- Multi-scale image scanning
- Real-time computer vision processing
- Webcam integration with OpenCV

---

## Output
- Live webcam feed
- Green rectangles highlighting detected faces
- Smooth real-time detection performance

---

## How to Run the Project

### Prerequisites
Install required library:
- opencv-python

---

### Steps
1. Ensure a webcam is connected
2. Verify the Haar Cascade XML file path
3. Run the Python script
4. Observe:
   - Real-time face detection
   - Bounding boxes drawn on detected faces
5. Press **'p'** to exit

---

## Learning Outcomes
- Understanding traditional face detection techniques
- Experience with OpenCV video processing
- Ability to implement real-time object detection
- Knowledge of Haar Cascades and their limitations

---

## Limitations
- Sensitive to lighting conditions
- Less accurate compared to deep learning-based detectors
- May struggle with occlusion or non-frontal faces

---

## Future Improvements
- Use deep learning-based face detectors (DNN, MTCNN)
- Improve robustness under varying lighting
- Detect facial landmarks
- Integrate face recognition
- Optimize detection speed

---

## Use Case
This project is suitable for:
- Computer vision beginners
- Academic lab assignments
- Classical face detection demonstrations
- Preprocessing step for face recognition systems

---

## Author
Developed as an educational computer vision project demonstrating real-time face detection using Haar Cascade classifiers and OpenCV.

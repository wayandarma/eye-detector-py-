# Eye State Detector

## Overview

This Python program uses computer vision techniques to detect a person's eye state (open or closed) using a webcam. It can identify when a person has had their eyes closed for an extended period (5 seconds) and provides time-stamped console output for eye closure events.

## Features

- Real-time eye state detection using a webcam
- Console output for prolonged eye closure events (5 seconds or more)
- Visual display of current eye state on the video feed
- Facial landmark visualization (optional)

## Requirements

- Python 3.6 or higher
- OpenCV (cv2)
- dlib
- NumPy
- SciPy

## Installation

1. Clone this repository or download the `eye_state_detector.py` file.

2. Install the required Python packages:

   ```
   pip install opencv-python dlib numpy scipy
   ```

3. Download the shape predictor file:
   ```
   curl -L "https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2" -o shape_predictor_68_face_landmarks.dat.bz2
   bzip2 -d shape_predictor_68_face_landmarks.dat.bz2
   ```
   Ensure this file is in the same directory as the Python script.

## Usage

Run the script using Python:

```
python eye_state_detector.py
```

- The program will open your default webcam and start detecting eye states.
- A window will appear showing the video feed with facial landmarks (if enabled) and the current eye state.
- When eyes are detected as closed for 5 seconds, details will be printed to the console.
- Press 'q' to quit the program.

## How It Works

1. **Face Detection**: The program uses dlib's face detector to locate faces in each frame of the video.

2. **Facial Landmark Detection**: Once a face is detected, dlib's shape predictor is used to identify 68 facial landmarks, including those around the eyes.

3. **Eye Aspect Ratio (EAR) Calculation**: The program calculates the Eye Aspect Ratio, which is a measure of eye openness based on the positions of the eye landmarks.

4. **Eye State Determination**: If the EAR falls below a certain threshold, the eyes are considered closed.

5. **Prolonged Closure Detection**: The program tracks how long the eyes remain closed. If they stay closed for 5 seconds or more, it logs this event with timestamps.

6. **Visual Feedback**: The current eye state (open or closed) is displayed on the video feed, and facial landmarks are optionally drawn.

## Customization

- Adjust the `sleep_threshold` variable to change the duration required for detecting prolonged eye closure.
- Modify the EAR threshold in the `check_eyes_closed` function to fine-tune eye closure detection sensitivity.
- Comment out or modify the facial landmark drawing code to change the visual output.

## Limitations

- The accuracy of detection can be affected by lighting conditions, camera quality, and face orientation.
- This program is designed for demonstration and educational purposes and may not be suitable for critical applications without further refinement.

## Troubleshooting

- If you encounter issues with dlib installation, ensure you have the necessary build tools installed on your system.
- For webcam access issues, check your system permissions and ensure no other program is using the camera.

## License

This project is open-source and available under the MIT License.

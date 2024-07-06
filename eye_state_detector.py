import cv2
import dlib
import numpy as np
from scipy.spatial import distance
from datetime import datetime, timedelta
from playsound import playsound
def calculate_EAR(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def check_eyes_closed(shape):
    left_eye = shape[42:48]
    right_eye = shape[36:42]
    
    left_EAR = calculate_EAR(left_eye)
    right_EAR = calculate_EAR(right_eye)
    
    avg_EAR = (left_EAR + right_EAR) / 2.0
    return avg_EAR < 0.25  # Adjust this threshold as needed

def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    
    eyes_closed_start = None
    sleep_threshold = timedelta(seconds=5)
    sleeping = False
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        
        for face in faces:
            shape = predictor(gray, face)
            shape = np.array([(shape.part(i).x, shape.part(i).y) for i in range(68)])
            
            if check_eyes_closed(shape):
                if eyes_closed_start is None:
                    eyes_closed_start = datetime.now()
                elif not sleeping and datetime.now() - eyes_closed_start >= sleep_threshold:
                    sleeping = True
                    sleep_start_time = eyes_closed_start.strftime("%Y-%m-%d %H:%M:%S")
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"The object closed their eyes at: {sleep_start_time}")
                    print(f"5 seconds have passed. Current time: {current_time}")
                    print(f"Total eyes-closed duration: {datetime.now() - eyes_closed_start}")

                    playsound("sound.mp3")
            else:
                if sleeping:
                    eyes_open_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"The object opened their eyes at: {eyes_open_time}")
                    print(f"Total eyes-closed duration: {datetime.now() - eyes_closed_start}")
                eyes_closed_start = None
                sleeping = False
            
            # Draw facial landmarks (optional)
            for (x, y) in shape:
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
        
        # Display eye state on frame
        status_text = "Eyes: Closed" if eyes_closed_start else "Eyes: Open"
        cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255) if eyes_closed_start else (0, 255, 0), 2)
        
        cv2.imshow("Frame", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
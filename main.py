import cv2
import mediapipe as mp
import pyautogui

# Initialize webcam and face mesh detector
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Parameters to adjust sensitivity
mouse_sensitivity = 1.5  # Adjust this value to change sensitivity

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
if landmark_points:
        landmarks = landmark_points[0].landmark

        # Control mouse movement using eye landmarks
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
            if id == 1:
                screen_x = screen_w * landmark.x * mouse_sensitivity
                screen_y = screen_h * landmark.y * mouse_sensitivity
                pyautogui.moveTo(screen_x, screen_y)

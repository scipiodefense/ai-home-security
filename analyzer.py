# analyzer.py

import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose

def analyze_video(file_path):
    cap = cv2.VideoCapture(file_path)
    pose = mp_pose.Pose()
    fall_detected = False
    person_detected = 0

    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(frame_rate)  # sample 1 frame per second
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb)

            if results.pose_landmarks:
                person_detected += 1
                landmarks = results.pose_landmarks.landmark

                # Estimate fall via horizontal body orientation
                shoulder_y = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y
                hip_y = landmarks[mp_pose.PoseLandmark.LEFT_HIP].y
                if abs(shoulder_y - hip_y) < 0.05:  # flat pose
                    fall_detected = True

        frame_count += 1

    cap.release()

    if fall_detected:
        return "⚠️ Fall detected in video!"
    elif person_detected > 0:
        return f"🚶 Person passed by in {person_detected} sampled frames."
    else:
        return "No person detected."


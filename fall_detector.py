import cv2
import numpy as np
import face_recognition

def detect_fall(video_path):
    cap = cv2.VideoCapture(video_path)
    fall_detected = False

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        if frame_count % 10 != 0:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if w > 50 and h > 50:
                aspect_ratio = float(w) / h
                if aspect_ratio > 1.7:  # wide body — possibly fallen
                    fall_detected = True
                    break
        if fall_detected:
            break

    cap.release()
    return fall_detected


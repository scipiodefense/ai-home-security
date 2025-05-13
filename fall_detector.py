import cv2

def detect_fall(video_path):
    cap = cv2.VideoCapture(video_path)
    fall_detected = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        height, width = frame.shape[:2]
        resized = cv2.resize(frame, (320, 240))
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)

        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            aspect_ratio = float(w) / h if h != 0 else 0
            if w > 50 and h > 50 and aspect_ratio > 1.7:
                fall_detected = True
                break
        if fall_detected:
            break

    cap.release()
    return fall_detected


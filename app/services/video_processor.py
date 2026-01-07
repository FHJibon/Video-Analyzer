import cv2

def extract_frames(video_path, fps=1):
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    step = frame_rate * fps

    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if count % step == 0:
            frames.append(frame)
        count += 1

    cap.release()
    return frames
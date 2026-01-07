from fastapi import FastAPI, UploadFile
import shutil
from app.services.video_processor import extract_frames
from app.services.vision import detect_players
from app.services.report import generate_report

app = FastAPI()

@app.post("/upload")
async def analyze_video(file: UploadFile):
    video_path = f"temp_{file.filename}"

    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    frames = extract_frames(video_path)
    metrics = detect_players(frames)
    report = generate_report(metrics)

    return {
        "metrics": metrics,
        "report": report
    }
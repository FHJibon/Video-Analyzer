from ultralytics import YOLO

model = YOLO("yolov8n.pt")  

def detect_players(frames):
    player_counts = []

    for frame in frames:
        results = model(frame, verbose=False)
        count = 0
        for r in results:
            for c in r.boxes.cls:
                if int(c) == 0:  
                    count += 1
        player_counts.append(count)

    return {
        "avg_players_visible": sum(player_counts) / len(player_counts),
        "max_players_visible": max(player_counts)
    }
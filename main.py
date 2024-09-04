import av
from ultralytics import YOLO
import json

def extract_frames(video_path, interval=0.5):
    container = av.open(video_path)
    frames = []
    timestamps = []

    for frame in container.decode(video=0):
        if frame.time >= len(frames) * interval:
            img = frame.to_image()  # Convert frame to PIL Image
            frames.append(img)
            timestamps.append(frame.time)
            
    return frames, timestamps

def detect_logos(frames, timestamps):
    # Load YOLOv8 model (fine-tuned on Pepsi and CocaCola logos)
    model = YOLO('best.pt')

    pepsi_timestamps = []
    cocacola_timestamps = []

    for idx, frame in enumerate(frames):
        results = model(frame)
        
        for result in results[0].boxes:
            label = model.names[int(result.cls)]
            if label == 'Pepsi':
                pepsi_timestamps.append(timestamps[idx])
            elif label == 'CocaCola':
                cocacola_timestamps.append(timestamps[idx])

    return pepsi_timestamps, cocacola_timestamps

def process_video(video_path, output_json='output.json', interval=0.5):
    frames, timestamps = extract_frames(video_path, interval)
    pepsi_timestamps, cocacola_timestamps = detect_logos(frames, timestamps)

    output = {
        "Pepsi_pts": pepsi_timestamps,
        "CocaCola_pts": cocacola_timestamps
    }

    with open(output_json, 'w') as f:
        json.dump(output, f, indent=4)
    
    print(f"Detection results saved to {output_json}")
    

# Example usage
if __name__ == "__main__":
    video_path = '/content/Make_Amazing_Cups_Using_Soda_Cans_and_earn_money.mp4'  # Replace with your video file path
    process_video(video_path)

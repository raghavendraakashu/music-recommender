# music-recommender.py

from deepface import DeepFace
import cv2
from collections import Counter
import webbrowser

# Map detected emotions to YouTube playlists/videos
emotion_youtube = {
    "happy": "https://www.youtube.com/watch?v=NvEKBcEa4uM&list=RDNvEKBcEa4uM&start_radio=1",   # Happy Song
    "sad": "https://www.youtube.com/watch?v=TdrL3QxjyVw&list=RDTdrL3QxjyVw&start_radio=1",     # Sad Song
    "angry": "https://www.youtube.com/watch?v=Ug9A82D8bqE&list=RDUg9A82D8bqE&start_radio=1",   # Angry Song
    "neutral": "https://www.youtube.com/watch?v=B9KFb_fmvV8&list=RDB9KFb_fmvV8&start_radio=1", # LoFi / Chill
}

# --- Emotion Detection ---
cap = cv2.VideoCapture(0)
emotions = []

print("📷 Capturing 10 frames, please hold still...")

for i in range(10):  # capture 10 frames
    ret, frame = cap.read()
    if ret:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotions.append(result[0]['dominant_emotion'])

# Release webcam
cap.release()
cv2.destroyAllWindows()

# Find most frequent emotion
dominant_emotion = Counter(emotions).most_common(1)[0][0]
print("Final Detected Emotion:", dominant_emotion)

# --- Open YouTube ---
if dominant_emotion in emotion_youtube:
    youtube_link = emotion_youtube[dominant_emotion]
    webbrowser.open(youtube_link)
    print(f"🎵 Opening YouTube for {dominant_emotion} mood: {youtube_link}")
else:
    print("No YouTube link mapped for this emotion.")

import os
import cv2
import mediapipe as mp
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

dataset_path = "dataset"

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True)

data = []
labels = []

print("Starting dataset reading...")

for label in os.listdir(dataset_path):

    folder = os.path.join(dataset_path, label)

    if not os.path.isdir(folder):
        continue

    print("Reading folder:", label)

    for img_name in os.listdir(folder):

        img_path = os.path.join(folder, img_name)

        img = cv2.imread(img_path)

        if img is None:
            continue

        img = cv2.resize(img, (300,300))

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                landmarks = []

                # 🔹 Normalize landmarks (accuracy improvement)
                x_base = hand_landmarks.landmark[0].x
                y_base = hand_landmarks.landmark[0].y

                for lm in hand_landmarks.landmark:
                    landmarks.append(lm.x - x_base)
                    landmarks.append(lm.y - y_base)

                data.append(landmarks)
                labels.append(label)

print("Images processed:", len(data))

data = np.array(data)

print("Training model...")

model = RandomForestClassifier()
model.fit(data, labels)

pickle.dump(model, open("sign_model.pkl", "wb"))

print("✅ Model trained successfully!")
print("📁 Model saved as sign_model.pkl")
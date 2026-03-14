import cv2
import mediapipe as mp
import numpy as np
import pickle
from collections import Counter

# Load trained model
model = pickle.load(open("sign_model.pkl", "rb"))

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7
)

cap = cv2.VideoCapture(0)

predictions = []

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            landmarks = []
            x_list = []
            y_list = []

            h, w, c = frame.shape

            for lm in hand_landmarks.landmark:
                x = int(lm.x * w)
                y = int(lm.y * h)

                x_list.append(x)
                y_list.append(y)

            # Normalize landmarks
            x_base = hand_landmarks.landmark[0].x
            y_base = hand_landmarks.landmark[0].y

            for lm in hand_landmarks.landmark:
                landmarks.append(lm.x - x_base)
                landmarks.append(lm.y - y_base)

            # Prediction
            prediction = model.predict([np.array(landmarks)])[0]

            predictions.append(prediction)

            # Keep last 10 predictions
            if len(predictions) > 10:
                predictions.pop(0)

            # Most common prediction
            stable_prediction = Counter(predictions).most_common(1)[0][0]

            x1 = min(x_list)
            y1 = min(y_list)
            x2 = max(x_list)
            y2 = max(y_list)

            cv2.rectangle(frame,(x1-20,y1-20),(x2+20,y2+20),(0,255,0),2)

            cv2.putText(frame,
                        stable_prediction,
                        (x1,y1-30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0,0,255),
                        2)

            mp_draw.draw_landmarks(frame,
                                   hand_landmarks,
                                   mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Sign Language Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
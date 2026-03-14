import cv2
import os
import string

dataset_path = "dataset"
letters = list(string.ascii_uppercase)

cap = cv2.VideoCapture(0)

img_size = 300
images_per_letter = 200

for letter in letters:
    
    count = 0
    folder = os.path.join(dataset_path, letter)

    print(f"\nCollecting images for letter: {letter}")
    print("Press 'S' to start")

    while True:

        ret, frame = cap.read()

        cv2.rectangle(frame,(100,100),(400,400),(0,255,0),2)
        roi = frame[100:400,100:400]

        cv2.putText(frame,f"Letter: {letter}",(10,50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

        cv2.imshow("Dataset Collection", frame)

        key = cv2.waitKey(1)

        if key == ord('s'):
            break

    while count < images_per_letter:

        ret, frame = cap.read()

        cv2.rectangle(frame,(100,100),(400,400),(0,255,0),2)
        roi = frame[100:400,100:400]

        roi = cv2.resize(roi,(img_size,img_size))

        file_path = os.path.join(folder,f"{count}.jpg")

        cv2.imwrite(file_path, roi)

        count += 1

        cv2.putText(frame,f"Collecting {letter}: {count}/{images_per_letter}",
                    (10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

        cv2.imshow("Dataset Collection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print(f"{letter} completed!")

cap.release()
cv2.destroyAllWindows()

print("Dataset collection finished!")
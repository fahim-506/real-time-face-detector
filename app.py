import os
import cv2
import time

cap = cv2.VideoCapture(0)

num_persons = int(input("Enter number of persons: "))
images_per_person = 50

for person_id in range(num_persons):

    person_name = input(f"Enter name/ID for person {person_id + 1}: ")

    save_folder = f"dataset/{person_name}"
    os.makedirs(save_folder, exist_ok=True)

    print(f"\nCollecting data for {person_name}... Look at the camera.")

    img_count = 0
    time.sleep(2)  

    while img_count < images_per_person:

        ret, frame = cap.read()

        if not ret:
            print("Failed to access webcam")
            break


        text = f"{person_name} | Image: {img_count + 1}/{images_per_person}"
        cv2.putText(
            frame,
            text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )


        cv2.imshow("Webcam", frame)


        img_name = f"{save_folder}/{person_name}_{img_count:03d}.jpg"
        cv2.imwrite(img_name, frame)

        print(f"Saved: {img_name}")

        img_count += 1


        time.sleep(0.2)

        # press q to stop early
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
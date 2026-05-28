from ultralytics import YOLO
import cv2

model = YOLO("best.pt")

print("Loaded classes:", model.names)

cap = cv2.VideoCapture(0)

CONF_THRESHOLD = 0.75

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.25, verbose=True)[0]

    for box in results.boxes:

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls_id = int(box.cls[0])

        name = model.names[cls_id]

        if conf < CONF_THRESHOLD:
            label = "Unknown"
            color = (0, 0, 255)
        else:
            label = f"{name} {conf:.2f}"
            color = (0, 255, 0)

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

    cv2.imshow("FACE DETECTION (FINAL)", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print("Loaded classes:", model.names)
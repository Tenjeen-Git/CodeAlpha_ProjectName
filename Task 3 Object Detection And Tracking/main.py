import cv2
from ultralytics import YOLO


def run_detection_tracking(source=0):
    model = YOLO("yolov8s.pt")

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("Error: Could not open webcam or video file.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Video ended or camera disconnected.")
            break

        results = model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            conf=0.6,
            iou=0.5
        )

        output_frame = results[0].plot()

        cv2.imshow("Object Detection and Tracking", output_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_detection_tracking(0)
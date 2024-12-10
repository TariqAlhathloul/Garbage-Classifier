import cv2
from ultralytics import YOLO
import numpy as np
import torch
from message import display_text



labels = {0: 'BIODEGRADABLE', 1: 'CARDBOARD', 2: 'GLASS', 3: 'METAL', 4: 'PAPER', 5: 'PLASTIC'} 
RECYCLABLE = [1, 4]
NON_RECYCLABLE = [0, 2, 3, 5]


def draw_bbox(frame: np.ndarray, bbox: torch.Tensor, color=(0, 0, 255), thickness: int =2):
    """
    the function draws a bounding box on an image
    we will use it to draw bounding boxes only on the violated cars
    """
    #convert to numpy
    pt1 = bbox.xywh[0][0:2].numpy()
    pt2 = bbox.xywh[0][2:4].numpy()
    #calculate top left and bottom right points
    top_left = (int(pt1[0] - pt2[0] / 2), int(pt1[1] - pt2[1] / 2))
    bottom_right = (int(pt1[0] + pt2[0] / 2), int(pt1[1] + pt2[1] / 2))
    #draw the bounding box
    cv2.rectangle(frame, top_left, bottom_right, color, thickness)
    return frame


def _detect() -> None:
    """
    detect and show the output on the LCD text screen.
    """
    model = YOLO("./weights/best_2.pt", "detect", True)
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot Open the Camera.")
        print("exiting...")
        exit()

    while True:
        success, frame = cap.read()
        if not success:
            print("Cannot capture video.")
            print("exiting...")
            exit()

        results = model(frame, imgsz=640, conf=0.7)

        if len(results) > 0:

            for box in results[0].boxes:
                cls_id = int(box.cls)
                if cls_id in RECYCLABLE:
                    display_text(labels[cls_id], 1, 1)
                elif cls_id in NON_RECYCLABLE:
                    display_text(labels[cls_id], 1, 1)

                else:
                    display_text("Unknown", 1, 2)
                    
    cap.release()


def detect_LCD() -> None:
    """
    detect and show the output on the LCD text screen.
    """
    model = YOLO("./weights/best_2.onnx", "detect", True)
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot Open the Camera.")
        print("exiting...")
        exit()

    while True:
        success, frame = cap.read()
        if not success:
            print("Cannot capture video.")
            print("exiting...")
            exit()

        results = model(frame, imgsz=640, conf=0.6)

        if len(results) > 0:

            for box in results[0].boxes:
                cls_id = int(box.cls)
                if cls_id in RECYCLABLE:
                    display_text("Recyclable", 1, 2)
                elif cls_id in NON_RECYCLABLE:
                    display_text("Non-Recyclable", 1, 2)
                else:
                    display_text("Unknown", 1, 2)

    cap.release()
    



def live_detect() -> None:
    """
    detect and show the output on the live video feed.
    """
    model = YOLO("./weights/best_2.onnx", "detect", True)
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot Open the Camera.")
        print("exiting...")
        exit()

    frame_count = 0
    while True:
        success, frame = cap.read()
        if not success:
            print("Cannot capture video.")
            print("exiting...")
            break

        results = model(frame, imgsz=640, conf=0.6)

        if len(results) > 0 and frame_count % 10 == 0:

            for box in results[0].boxes:
                cls_id = int(box.cls)
                draw_bbox(frame, box)
                if cls_id in RECYCLABLE:
                    display_text("Recyclable", 1, 2)
                elif cls_id in NON_RECYCLABLE:
                    display_text("Non-Recyclable", 1, 2)
                else:
                    display_text("Unknown", 1, 2)


        cv2.imshow('Live', frame)
        frame_count += 1
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()




if __name__ == "__main__":
    _detect()
    #detect_LCD()
    #live_detect()
    
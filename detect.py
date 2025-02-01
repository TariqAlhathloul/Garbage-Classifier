import cv2
from ultralytics import YOLO
from message import display_text
from adafruit_servokit import ServoKit
from time import sleep

# All the classes
labels = {0: 'biodegradable', 1: 'cardboard', 2: 'glass', 3: 'gloves', 4: 'masks', 5: 'medicines', 6: 'metal', 7: 'paper', 8: 'plastic'}
# Array of the recyclable
RECYCLABLE = [1, 7]
# Array of the non-recyclable garbage
NON_RECYCLABLE = [0, 2, 3, 4, 5, 6, 8]
# Line 1 and 2 on the LCD screen
lines = [1, 2]

def rec():
    kit = ServoKit(channels=16)
    kit.servo[0].angle = 120
    sleep(6)
    kit.servo[0].angle = 0

def non_rec():
    kit = ServoKit(channels=16)
    kit.servo[1].angle = 0
    sleep(6)
    kit.servo[1].angle = 120
    
def detect() -> None:
    """
    detect and show the output on the live video feed.
    """
    model = YOLO("./models/model.pt", "detect", True)
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot Open the Camera.")
        print("exiting...")
        exit()

    frame_count = 0
    try:
        while True:
            success, frame = cap.read()
            if not success:
                print("Cannot capture video.")
                print("exiting...")
                break

            if frame_count % 20 == 0:
                # send frames to the model
                results = model(frame)

                for res in results:
                    cls_id = int(res.probs.top1)
                    conf = res.probs.top1conf
                    if cls_id != 4 and conf > 0.90:
                        if cls_id in RECYCLABLE:
                            text = [labels[cls_id], "RECYCLABLE"]
                            display_text(text, lines, 6)
                            #rec()
                        elif cls_id in NON_RECYCLABLE:
                            text = [labels[cls_id], "NON-RECYCLABLE"]
                            display_text(text, lines, 6)
                            #non_rec()
                    else:
                        display_text(["No", "Detection"], lines, 3)
            frame_count += 1

    except KeyboardInterrupt:
        cap.release()
        exit()


if __name__ == "__main__":
   detect()
    
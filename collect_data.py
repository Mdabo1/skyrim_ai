import numpy as np
import cv2
from utils.windowcapture import WindowCapture
from ultralytics import YOLO
from utils.getkeys import key_check
from utils.getkeys import mouse_check
import os


# Load YOLO Skyrim Model
model = YOLO("yolo_skyrim.pt")

# Capture Skyrim window
wincap = WindowCapture("Skyrim")

classes = ["Human-Like"]

colors = np.random.uniform(0, 255, size=(len(classes), 3))


def keys_to_output(keys):
    #         W A S D leftclick 
    output = [0, 0, 0, 0, 0]
    if "W" in keys:
        output[0] = 1
    elif "A" in keys:
        output[1] = 1
    elif "S" in keys:
        output[2] = 1
    elif "D" in keys:
        output[3] = 1
    elif "leftClick" in keys:
        output[4] = 1
    return output


file_name = "training_data.npy"

if os.path.isfile(file_name):
    print("File exists, loading previous data!")
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print("File does not exist")
    training_data = []

while True:

    # capture game screen
    screen = wincap.get_screenshot()
    img = cv2.resize(screen, (320, 240), fx=0.4, fy=0.3, interpolation=cv2.INTER_AREA)

    # concatenate pressed keys and mouse movements
    keys = key_check()
    output = keys_to_output(keys) + mouse_check()

    # predict NPC's bounding boxes
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

            # put box on image
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 200, 0), 3)

    # add X (images) and Y (key inputs) to training data
    training_data.append([img, output])
    cv2.imshow("Window", img)

    if len(training_data) % 10000 == 0:
        print(len(training_data))
        np.save(file_name, training_data)
        break
    if cv2.waitKey(1) == ord("q"):
        break

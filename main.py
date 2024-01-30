import numpy as np
import cv2
from windowcapture import WindowCapture
import math
from ultralytics import YOLO
from getkeys import key_check
import os

# Load Yolo
model = YOLO("best.pt")

wincap = WindowCapture("Skyrim")

classes = ["Human-Like"]

colors = np.random.uniform(0, 255, size=(len(classes), 3))


def keys_to_output(keys):
    #         W A S D shift alt space
    output = [0, 0, 0, 0, 0, 0, 0]
    if "W" in keys:
        output[0] = 1
    elif "A" in keys:
        output[1] = 1
    elif "S" in keys:
        output[2] = 1
    elif "D" in keys:
        output[3] = 1
    elif "alt" in keys:
        output[4] = 1
    elif "shift" in keys:
        output[5] = 1
    elif "space" in keys:
        output[6] = 1
    return output


file_name = "training_data.npy"

if os.path.isfile(file_name):
    print("File exists, loading previous data!")
    training_data = list(np.load(file_name))
else:
    print("File does not exist")
    training_data = []

while True:
    screen = wincap.get_screenshot()
    img = cv2.resize(screen, (800, 600), fx=0.4, fy=0.3)
    keys = key_check()
    output = keys_to_output(keys)
    training_data.append([img, output])
    # success, img = wincap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 200, 0), 3)

            # confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)

            # class name
            cls = int(box.cls[0])
            print("Class name -->", classes[cls])

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

    cv2.imshow("Window", img)

    if len(training_data) % 100 == 0:
        print(len(training_data))
        np.save(file_name, training_data)

    if cv2.waitKey(1) == ord("q"):
        break

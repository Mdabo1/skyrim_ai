import torch
import cv2
import numpy as np
from ultralytics import YOLO
from resnet18_torchvision import build_model
import time
import pydirectinput
from utils.windowcapture import WindowCapture
from utils.direct_keys import press_key, release_key, move_mouse, W, A, S, D, X

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
wincap = WindowCapture("Skyrim")

# load YOLO-skyrim model

model_cv = YOLO("yolo_skyrim.pt")

# load trained resnet-18 model

model_pt = build_model(pretrained=False, fine_tune=False, num_classes=9)
state_dict = torch.load("resnet-500e-64b-0354470.pt", map_location="cuda:0")
model_pt.load_state_dict(state_dict)
model_pt.to(device)
model_pt.eval()

pydirectinput.FAILSAFE = False

WIDTH = 320
HEIGHT = 240

while True:
    # predict bounding boxes
    screen = wincap.get_screenshot()
    img = cv2.resize(
        screen, (WIDTH, HEIGHT), fx=0.4, fy=0.3, interpolation=cv2.INTER_AREA
    )
    results = model_cv(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 200, 0), 3)

    img = np.array(img).reshape(3, HEIGHT, WIDTH)
    img = torch.from_numpy(img).float()
    img = img.to(device)

    # predict keyboard outputs
    with torch.no_grad():
        preds = model_pt(img.unsqueeze(0))
        probs = torch.nn.functional.softmax(preds, dim=1)
        _, pred = torch.max(preds, 1)
        pred_prob = probs[0][pred].item()

        # add some randomness (if no roundoff error like sum of probs 0.99999)
        p = np.array(probs.tolist()[0]).astype("float64")
        p = p / sum(p)

        if sum(p) == 1.0:
            pred = np.random.choice(len(probs.tolist()[0]), 1, p=p)[0]
            print("Confidence (random choice): ", probs[0][pred].item() * 100, "%")

        else:
            print("Confidence: ", pred_prob * 100, "%")

        if pred == 0:
            print("W")
            press_key(W)
            time.sleep(0.1)
            release_key(W)
        elif pred == 1:
            print("A")
            press_key(A)
            time.sleep(0.1)
            release_key(A)
        elif pred == 2:
            print("S")
            press_key(S)
            time.sleep(0.1)
            release_key(S)
        elif pred == 3:
            print("D")
            press_key(D)
            time.sleep(0.1)
            release_key(D)
        elif pred == 4:
            print("left click")
            press_key(X)
            time.sleep(0.3)
            release_key(X)
        elif pred == 5:
            print("cursor left")
            x = -100
            y = 0
            move_mouse(x, y)
        elif pred == 6:
            print("cursor right")
            x = 100
            y = 0
            move_mouse(x, y)
        elif pred == 7:
            print("cursor up")
            x = 0
            y = -50
            move_mouse(x, y)
        elif pred == 8:
            print("cursor down")
            x = 0
            y = 50
            move_mouse(x, y)

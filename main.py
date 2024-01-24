import numpy as np
import cv2
import time
from windowcapture import WindowCapture
from directkeys import ReleaseKey, PressKey, W, A, S, D, LM, RM
import math
from ultralytics import YOLO

# Load Yolo
model = YOLO("best.pt")

wincap = WindowCapture("Skyrim")

classes = ["Human-Like"]

colors = np.random.uniform(0, 255, size=(len(classes), 3))


# def main():
#     last_time = time.time()
#     while True:
#         screen = wincap.get_screenshot()
#         img = cv2.resize(screen, (800, 600), fx=0.4, fy=0.3)
#         height, width, channels = img.shape
#         blob = cv2.dnn.blobFromImage(
#             img, 0.00392, (416, 416), (0, 0, 0), True, crop=False
#         )
#         net.setInput(blob)
#         outs = net.forward(outputlayers)

#         # Showing info on screen / get confidence score of algorithm in detecting an object in blob
#         class_ids = []
#         confidences = []
#         boxes = []
#         for out in outs:
#             for detection in out:
#                 scores = detection[5:]
#                 class_id = np.argmax(scores)
#                 confidence = scores[class_id]
#                 if confidence > 0.5:
#                     # object detected
#                     center_x = int(detection[0] * width)
#                     center_y = int(detection[1] * height)
#                     w = int(detection[2] * width)
#                     h = int(detection[3] * height)
#                     # rectangle co-ordinaters
#                     x = int(center_x - w / 2)
#                     y = int(center_y - h / 2)
#                     boxes.append([x, y, w, h])  # put all rectangle areas
#                     confidences.append(
#                         float(confidence)
#                     )  # how confidence was that object detected and show that percentage
#                     class_ids.append(class_id)  # name of the object that was detected
#         indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.6)
#         font = cv2.FONT_HERSHEY_PLAIN
#         for i in range(len(boxes)):
#             if i in indexes:
#                 x, y, w, h = boxes[i]
#                 label = str(classes[class_ids[i]])
#                 color = colors[i]
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                 cv2.putText(img, label, (x, y + 30), font, 1, (255, 255, 255), 2)
#         print("FPS {}".format(1 / (time.time() - last_time)))
#         last_time = time.time()
#         cv2.imshow("window", img)
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             cv2.destroyAllWindows()
#             break


while True:
    screen = wincap.get_screenshot()
    img = cv2.resize(screen, (800, 600), fx=0.4, fy=0.3)

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
    if cv2.waitKey(1) == ord("q"):
        break

# main()

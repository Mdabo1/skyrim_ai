# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load("training_data_v2.npy", allow_pickle=True)


lefts = []
rights = []
forwards = []
backs = []
leftClicks = []
cursor_left = []
cursor_right = []
cursor_up = []
cursor_down = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice[0] == 1:  # W
        forwards.append([img, [1, 0, 0, 0, 0, 0, 0, 0, 0]])
    elif choice[1] == 1:  # A
        lefts.append([img, [0, 1, 0, 0, 0, 0, 0, 0, 0]])
    elif choice[2] == 1:  # S
        backs.append([img, [0, 0, 1, 0, 0, 0, 0, 0, 0]])
    elif choice[3] == 1:  # D
        rights.append([img, [0, 0, 0, 1, 0, 0, 0, 0, 0]])
    elif choice[4] == 1:  # leftClick
        leftClicks.append([img, [0, 0, 0, 0, 1, 0, 0, 0, 0]])
    elif choice[5] == 1:  # cursor left
        cursor_left.append([img, [0, 0, 0, 0, 0, 1, 0, 0, 0]])
    elif choice[6] == 1:  # cursor right
        cursor_left.append([img, [0, 0, 0, 0, 0, 0, 1, 0, 0]])
    elif choice[7] == 1:  # cursor up
        cursor_left.append([img, [0, 0, 0, 0, 0, 0, 0, 1, 0]])
    elif choice[8] == 1:  # cursor down
        cursor_left.append([img, [0, 0, 0, 0, 0, 0, 0, 0, 1]])
    else:
        print("no matches")


forwards = forwards[: len(backs)]
lefts = lefts[: len(backs)]
rights = rights[: len(backs)]
backs = backs[: len(backs)]
leftClicks = leftClicks[: len(backs)]
cursor_left = cursor_left[: len(backs)]
cursor_right = cursor_right[: len(backs)]
cursor_up = cursor_up[: len(backs)]
cursor_down = cursor_down[: len(backs)]

final_data = (
    forwards
    + lefts
    + rights
    + backs
    + leftClicks
    + cursor_left
    + cursor_right
    + cursor_up
    + cursor_down
)
shuffle(final_data)

print(
    len(forwards),
    len(lefts),
    len(rights),
    len(backs),
    len(leftClicks),
    len(cursor_left),
    len(cursor_right),
    len(cursor_up),
    len(cursor_down),
)
# np.save("training_data_v3.npy", final_data)

# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load("training_data.npy", allow_pickle=True)

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
rights = []
forwards = []
backs = []
leftClicks = []
mouseMovements = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice[0] == 1:  # W
        forwards.append([img, choice])
    elif choice[1] == 1:  # A
        lefts.append([img, choice])
    elif choice[2] == 1:  # S
        backs.append([img, choice])
    elif choice[3] == 1:  # D
        rights.append([img, choice])
    elif choice[5] == 1:  # leftClick
        leftClicks.append([img, choice])
    elif choice[7] or choice[8]:  # Either X movement or Y movement
        mouseMovements.append([img, [0, 0, 0, 0, 0, 0, 0, choice[7], choice[8]]])
    else:
        print("no matches")


forwards = forwards[: len(leftClicks)]
lefts = lefts[: len(leftClicks)]
rights = rights[: len(leftClicks)]
backs = backs[: len(leftClicks)]
leftClicks = leftClicks[: len(leftClicks)]
mouseMovements = mouseMovements[: len(leftClicks)]

final_data = forwards + lefts + rights + backs + leftClicks + mouseMovements
shuffle(final_data)

np.save("training_data_v2.npy", final_data)

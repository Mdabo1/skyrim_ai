import pandas as pd
import numpy as np

train_data = np.load("training_data.npy", allow_pickle=True)

df = pd.DataFrame(train_data)

# sort X movements and Y movements separately
data_x = []
data_y = []

for i in range(len(df)):
    data_x.append(df[1][i][-2])
    data_y.append(df[1][i][-1])

# make X movements binary
Xses_binary = []
for i in data_x:
    if i < 0:
        Xses_binary.append([1, 0])  # cursor moves left
    elif i > 0:
        Xses_binary.append([0, 1])  # cursor moves right
    else:
        Xses_binary.append([0, 0])  # no horizontal movement

# make Y movements binary
Yses_binary = []
for i in data_y:
    if i < 0:
        Yses_binary.append([1, 0])  # cursor moves up
    elif i > 0:
        Yses_binary.append([0, 1])  # cursor moves down
    else:
        Yses_binary.append([0, 0])  # no vertical movement

# add X and Y binary movements to dataset
for i in range(len(df)):
    df[1][i] = df[1][i][:-2] + Xses_binary[i] + Yses_binary[i]

# count by key inputs
counts = []
for i in range(9):
    count = 0
    for j in range(len(df)):
        if df[1][j][i]:
            count += 1
    counts.append(count)
print(counts)


df_numpy = df.to_numpy()
np.save("training_data_v2.npy", df_numpy)

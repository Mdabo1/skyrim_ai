import numpy as np
import torch 
from torch.utils.data import DataLoader, TensorDataset

def get_data(batch_size=64):
    # create data loaders
    data = np.load("training_data_v3.npy", allow_pickle=True)

    train = data[:20560]
    test = data[20560:]

    WIDTH = 320
    HEIGHT = 240

    train_X = np.array([i[0] for i in train]).reshape(-1, 3, HEIGHT, WIDTH)
    train_y = [i[1] for i in train]

    test_X = np.array([i[0] for i in test]).reshape(-1, 3, HEIGHT, WIDTH)
    test_y = [i[1] for i in test]

    train_X = torch.from_numpy(train_X)
    train_y = torch.Tensor(train_y)
    test_X = torch.from_numpy(test_X)
    test_y = torch.Tensor(test_y)

    train_dataset = TensorDataset(train_X, train_y)
    test_dataset = TensorDataset(test_X, test_y)

    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    valid_loader = DataLoader(test_dataset, batch_size=64, shuffle=True)
    return train_loader, valid_loader
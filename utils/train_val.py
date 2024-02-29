from tqdm import tqdm
import torch


# training function
def train(model, train_loader, optimizer, criterion, device):
    model.train()
    print("Training")
    train_running_loss = 0.0
    train_running_correct = 0
    counter = 0

    for i, data in tqdm(enumerate(train_loader), total=len(train_loader)):
        counter += 1

        image, labels = data
        image = image.to(device)
        labels = labels.to(device)
        optimizer.zero_grad()

        # forward pass
        outputs = model(image.float())
        # calculate the loss
        loss = criterion(outputs, labels)
        train_running_loss += loss.item()
        # calculate the accuracy
        _, preds = torch.max(outputs.data, 1)
        _, labels_max = torch.max(labels.data, 1)
        train_running_correct += (preds == labels_max).sum().item()
        # backpropagation
        loss.backward()
        # ipdate the weights
        optimizer.step()

    # loss and accuracy for the complete epoch
    epoch_loss = train_running_loss / counter
    epoch_acc = 100.0 * (train_running_correct / len(train_loader.dataset))
    return epoch_loss, epoch_acc


# validation function
def validate(model, valid_loader, criterion, device):
    model.eval()
    print("Validation")
    valid_running_loss = 0.0
    valid_running_correct = 0
    counter = 0

    with torch.no_grad():
        for i, data in tqdm(enumerate(valid_loader), total=len(valid_loader)):
            counter += 1

            image, labels = data
            image = image.to(device)
            labels = labels.to(device)
            # forward pass
            outputs = model(image.float())
            # calculate the loss
            loss = criterion(outputs.data, labels)
            valid_running_loss += loss.item()
            # calculate the accuracy
            _, preds = torch.max(outputs, 1)
            _, labels_max = torch.max(labels, 1)
            valid_running_correct += (preds == labels_max).sum().item()

    # loss and accuracy for the complete epoch
    epoch_loss = valid_running_loss / counter
    epoch_acc = 100.0 * (valid_running_correct / len(valid_loader.dataset))
    return epoch_loss, epoch_acc

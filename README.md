# Skyrim AI

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nurislam-ai/)

Based on YOLOv8 object detecting + ResNet18 model that combats NPCs in The Elder Scrolls V: Skyrim!  

![skyrim1_1](https://github.com/Mdabo1/skyrim_ai/assets/122386960/f72d0ff7-0a23-4d08-9ba7-4857626cda37)

## What's next?

- [x] [Train YOLOv8 model on Skyrim dataset](https://universe.roboflow.com/skyrim-ai/skyrim-ai)
- [x] [Train ResNet18 model to predict AI movements](https://github.com/Mdabo1/skyrim_ai/blob/main/train_ai.ipynb)
- [ ] Reinforcement Learning



### The Model of TWO Models:  
1) Training object detection model on custom Skyrim dataset to predict NPC's bounding boxes (YOLOv8 model) 
2) Training keyboard inputs and mouse movements from game screenshots with NPC' bounding boxes (ResNet-18 model)

More Details Below!

## YOLOv8 inference on game's NPCs
![yolo (3)](https://github.com/Mdabo1/skyrim_ai/assets/122386960/b0ac52ea-1bdd-4010-9092-e691bd5e36e3)

* Train/Val/Test split is 2158/478/480 images  
* Precision - 96.4%, Recall - 91.6%
* Dataset/Model link (Roboflow) - https://universe.roboflow.com/skyrim-ai/skyrim-ai

## ResNet18 keyboard and mouse prediction
![skyrim2 (3)](https://github.com/Mdabo1/skyrim_ai/assets/122386960/86b6b6b0-9190-4635-919c-8b174c708c83)

* Train/Val split is 20560/4112
* Trained on rtx 3060, 500 epochs with 64 batch size for 4 hours (no pretrain/no finetune, total number of parameters 11,181,129)
* Accuracy is 35.4770% :(
* The mouse movement problem*
* Stucking problem (as you see in gif above)** 

*The mouse movement problem - If human's mouse movements are not constant, (it can be 30 pixels right then 5 pixels up, 5 pixels down and 0 pixels in X direction) our AI moves it only to some specific value  

**Almost 70% of time it acts not human-like (we don't want that!) 

## Train and Val accuracy (ResNet18)
![Train and Val accuracy through 500 epochs](https://github.com/Mdabo1/skyrim_ai/blob/main/outputs/resnet_torchvision_accuracy-500e-64b.png)

## Acknowledgments

Originally inspired by Sentdex - https://github.com/Sentdex/pygta5


# Face Recognition

An AI face recognition simple script powered by openCV made for TFGS back in 2023 which purpose was to demonstrate how to combine it with an RPi and Arduino board to simulate a door opening when particular faces were detected


![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)


## Usage

This project was built with the sole puropose of being a demo in TFGS so it's just a super simple version of what could have been done

The script is meant to work with the following directory structure:
```
Main Project
├── Faces
│   ├── 0
│   │  ├── pic_1
│   │  ├── pic_2
│   │  ├── pic_3
│   │  ├── pic_n
│   ├── 1
│   │  ├── pic_1
│   │  ├── pic_2
│   │  ├── pic_3
│   │  ├── pic_n
│   ├── 2
│   │  ├── pic_1
│   │  ├── pic_2
│   │  ├── pic_3
│   │  ├── pic_n
│   ├── n
│   │  ├── pic_1
│   │  ├── pic_2
│   │  ├── pic_3
│   │  ├── pic_n
├── Model
│   ├── Trained_Model.yml
├── FaceRecon.py
├── ModelTrainer.py
└── haarcascade_frontalface_default.xml
```
To make this script work fine first we need to train a OpenCV AI Model using our pictures so we will run ModelTrainer.py and we'll get an yml files with our data like the one shown below

![Preview](http://davidpoza.es/Resources/GitResources/facePreview.png)

Consider your device specs in order to perform this training, with 10 pictures on 3 diferent folders in a Dynabook Toshiba Portégé X30L-J-159 I had a hard time and the yml file contained 125048 lines of data

## Continuation

Not a priority but if conditions are meet maybe I start developing this again with cleaner code and improved features

import cv2
import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split


class BrainTumorTraining:
    def __init__(self, noTumorDir, yesTumorDir):
        self.noTumorDir = noTumorDir
        self.yesTumorDir = yesTumorDir
        self.noTumor = os.listdir(noTumorDir)
        self.yesTumor = os.listdir(yesTumorDir)
        self.dataSet = []
        self.label = []  
        
    def ResizeAndConvertData(self):
        # Might want to make it into one func
        for imageName in self.noTumor:
            if (imageName.split(".")[1] == "jpg"):
                image = cv2.imread(self.noTumorDir + f"/{imageName}")
                image = Image.fromarray(image, "RGB")  # Converting colour model to RGB
                image = image.resize((640, 640))
                self.dataSet.append(np.array(image)), self.label.append(False) # Makeing array of images with no label
                
        for imageName in self.yesTumor:
            if (imageName.split(".")[1] == "jpg"):
                image = cv2.imread(self.yesTumorDir + f"/{imageName}")
                image = Image.fromarray(image, "RGB")  # Converting colour model to RGB
                image = image.resize((640, 640))   # Resizing image
                self.dataSet.append(np.array(image)), self.label.append(True) # Makeing array of images with yes label 
        
        dataSet = np.array(dataSet)
        label = np.array(label)
        xTrain, xTest, yTrain, yTest = train_test_split(dataSet, label, train_size= 0.67) # Splits the dataset into a training and test splits
        
        
        
                
        

test = BrainTumorTraining(noTumorDir = "BrainTumorDetection/no", yesTumorDir= "BrainTumorDetection/yes")
test.ResizeAndConvertData()
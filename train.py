import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

import pandas as pd

import os



import torch
import torch.nn as nn
import torchvision
from torchvision import datasets
from torch.utils.data import DataLoader
import torchvision.transforms as T
from torch.cuda.amp import GradScaler
from sklearn.metrics import accuracy_score
import resize
import safe_pil_loader
#import pandas as pd


train_transforms = T.Compose([
        T.Resize((224, 224)),
        T.RandomHorizontalFlip(),
        T.RandomRotation(degrees=10),
        T.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) 
    ])

test_transforms = T.Compose([
        T.Resize((224, 224)),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) 
])




    

        

    #image_data = np.load('images\women\testing_set','images\men\testing_set','images\women\training_set','images\men\training_set')
    #image_data = np.load('imgds.npy')     

image_data = datasets.ImageFolder(root=r"C:\Users\gauta\OneDrive\Documents\GitHub\injurydetection\images", transform=train_transforms, loader=safe_pil_loader)
#test_dataset = datasets.ImageFolder(root=TEST_PATH, transform=test_transforms, loader=safe_pil_loader)
BATCH_SIZE = 64
NUM_WORKERS = os.cpu_count() - 1

loader = DataLoader(image_data, batch_size=BATCH_SIZE, shuffle=True, num_workers=NUM_WORKERS)

#image_data = np.load('images\women\testing_set','images\men\testing_set','images\women\training_set','images\men\training_set')
#image_data = np.load('imgds.npy')
dataiter  = NotImplemented
images = NotImplemented
labels = NotImplemented
while True:
    print("yes")
    if __name__ == '__iter__':
            
            dataiter = iter(loader)
            images, labels = next(dataiter)
            break

if(images is not NotImplemented and labels is not NotImplemented):
        #test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=NUM_WORKERS)
        #labels = ['oval','rectangular','round','square']

        #import matplotlib.pyplot as plt
        #print(image_data.shape

        from skimage.color import rgb2gray
        #gray_data = rgb2gray(image_data)

        #seen = set()
        #for i, label in enumerate (labels):
        #   if label in seen:
        #      continue
        # seen.add(label)#

        from sklearn.model_selection import train_test_split
        #print(images.len())
        X_train, X_test, y_train, y_test = train_test_split(images,labels,train_size=0.8,test_size=0.2,random_state = 42)



        import cv2

            

        from sklearn.metrics import confusion_matrix
        images.shape
        reshaped_gray_data = images.reshape((-1,64*64))
        reshaped_gray_data.shape
        from sklearn import preprocessing
        le = preprocessing.LabelEncoder()
        le.fit(labels)
        y = le.transform(labels)
        #X_train, X_test, y_train, y_test = train_test_split(reshaped_gray_data,y,test_size=0.2,random_state = 42)

        print(X_train.shape)
        print(X_test.shape)
        print(y_train.shape)
        print(y_test.shape)



        from sklearn.linear_model import LogisticRegression

        logistic_model = LogisticRegression()

        logistic_model.fit(X_train, y_train)

        predictions = logistic_model.predict(X_test)

        from sklearn.metrics import accuracy_score

        score = accuracy_score(y_test, predictions)
        print('Logistic Regression Model Accuracy: {:.2%}'.format(score))
        matrix = confusion_matrix(y_test, predictions)
        print(matrix.diagonal()/matrix.sum(axis=1))

        print(le.classes_)

        print(set(labels))

        from sklearn.metrics import confusion_matrix

        from sklearn.neighbors import KNeighborsClassifier


        neigh = KNeighborsClassifier(n_neighbors=1)

        neigh.fit(X_train,y_train)

        prediction = neigh.predict(X_test)


        score = accuracy_score(y_test, prediction)
        print('K Nearest Neighbor Model Accuracy: {:.2%}'.format(score))

        matrix = confusion_matrix(y_test, predictions)
        print(matrix.diagonal()/matrix.sum(axis=1))

        print(le.classes_)




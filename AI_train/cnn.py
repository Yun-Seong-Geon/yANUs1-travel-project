import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from keras import layers
from keras.utils import plot_model
from keras.layers import BatchNormalization
from keras.layers import MaxPooling2D
import os
import matplotlib.pyplot as plt

# #CNN 모델 1
# def model():
#     model = keras.Sequential()

#     model.add(layers.Conv2D(64, (15, 15), activation='relu',input_shape=(256,256,3),padding='same',strides=(3,3)))
#     model.add(BatchNormalization())
#     model.add(MaxPooling2D(pool_size=(8,8)))

#     model.add(layers.Conv2D(64, (7, 7), activation='relu'), padding='same',strides=(2,2))
#     model.add(BatchNormalization())
#     model.add(MaxPooling2D(pool_size=(5,5)))

#     model.add(layers.Conv2D(32, (5, 5), activation='relu'), padding='same')
#     model.add(BatchNormalization())
#     model.add(MaxPooling2D(pool_size=(3,3)))

#     model.add(layers.Conv2D(16, (3, 3), activation='relu'), padding='same')
#     model.add(BatchNormalization())
#     model.add(MaxPooling2D(pool_size=(2,2)))

#     #DNN
#     model.add(layers.Flatten())
#     model.add(layers.Dense(512, activation='relu'))
#     model.add(2, activation='sigmoid')

#     return model

class img_processing:
    def img_label(path,region):
        categories = {
            'bigben' : 0 ,
            'santorini' : 1
        }
        label = []
        images = []

        img_file = os.listdir(path)
        for img in img_file:
            label.append(categories[region])
            image = keras.preprocessing.image.load_img(f'{path}/{img}',target_size=(256,256))
            imageArr = np.array(image)
            images.append(imageArr)
            
        return images,label
            

    def concat(path,region,X,Y):
        NEW_X = np.concatenate((X,np.array(img_processing.img_label(path,region)[0])),axis=0)
        NEW_Y = np.concatenate((Y,np.array(img_processing.img_label(path,region)[1])),axis=0)
        return NEW_X, NEW_Y 

def start():
    categories = [
        'bigben',
        'santorini'
        
    ] # 지역이름 추가하기

    images = np.empty((0,256,256,3)) # 배열 생성
    labels = np.empty(0) # 배열생성

    for cate in categories:
        images,labels = img_processing.concat(cate,cate,images,labels)
    print(images.shape,labels.shape)

if __name__ == '__main__':  
    start()

    




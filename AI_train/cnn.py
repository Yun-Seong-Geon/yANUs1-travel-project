import numpy as np
from tensorflow import keras
import os
import ai_fuction as af
class img_processing:
    def img_label(path,region):
        categories = af.categories
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
    categories = af.categories
    # 지역이름 추가하기

    images = np.empty((0,256,256,3)) # 배열 생성
    labels = np.empty(0) # 배열생성

    for cate in categories:
        images,labels = img_processing.concat(cate,cate,images,labels)
    print(images.shape,labels.shape)

if __name__ == '__main__':  
    start()

    




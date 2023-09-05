from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import train_model_v1 as v1
import tensorflow as tf
import tensorflow_hub as hub
import ai_fuction as af

def test(path):
    
    categories = af.categories

    #모델 이름 입력
    Mname = input('모델이름.h5 입력')

    #모델 불러오기
    with tf.keras.utils.custom_object_scope({'KerasLayer': hub.KerasLayer}):
        loaded_model = tf.keras.models.load_model(Mname)
    trainX,testX,trainY,testY = v1.split()

    #테스트


    #모델 예측 수행
    
    pred = loaded_model.predict(testX)
    
    test_image = keras.preprocessing.image.load_img(path, target_size=(256,256))
    imageArr = np.array(test_image)
    imageArr = imageArr / 255
    imageArr = imageArr.reshape(-1,256,256,3)

    pred = loaded_model.predict(imageArr)

    pred_labels = np.argmax(pred, axis = 1)

    #예측 결과 실행
    print(categories[int(pred_labels)])
    plt.title(categories[int(pred_labels)])
    plt.imshow(imageArr[0])
    plt.show()
def preparing(images):
    image_list = [np.array(img) for img in images]
    imageArr = np.stack(image_list, axis=0)
    imageArr = imageArr / 255.0
    return imageArr

def val():
    with tf.keras.utils.custom_object_scope({'KerasLayer': hub.KerasLayer}):
        loaded_model = tf.keras.models.load_model('AI_train/BigTransferModel.h5')
    
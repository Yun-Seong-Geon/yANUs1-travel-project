import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
from PIL import Image


def adobe(img)->str:

    categories = {
            0 : 'Bigben' ,
            1 : 'Santorini',
            2 : 'Matterhorn',
            3 : 'Grand_Canyon',
            4 : 'the_statue_of_liberty',
            5 : 'eiffel_tower' ,
            6 : 'Gold_gate_bridge', 
            7 : 'Osakajo', 
            8 : 'pisa_tower', 
            9 : 'ayasofya_camii' 
        }
    img=Image.open(img)
    #이미지 전처리 및 정규화
    img = np.array(img)
    print(img.shape)
    img = tf.image.resize(img, [256,256]) / 255.0

    #넘파이 배열의 차원 확장
    img = np.expand_dims(img, axis=0)
    #모델 불러오기
    model_name = 'BigTransferModel.h5'

    with tf.keras.utils.custom_object_scope({'KerasLayer': hub.KerasLayer}):
        model = tf.keras.models.load_model(model_name)

    #모델 예측
    pred = model.predict(img)
    pred_labels = np.argmax(pred, axis=1)

    return categories[pred_labels[0]]

print(adobe(r'test_image_1.jpg'))
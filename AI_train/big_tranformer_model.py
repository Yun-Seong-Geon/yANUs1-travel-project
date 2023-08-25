import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
import tensorflow_hub as hub
from keras.callbacks import EarlyStopping
import train_model_v1 as v1
import preprocessing as pp


def create_bit_model():
    model_url = "https://tfhub.dev/google/bit/m-r50x1/1"
    bit_model = tf.keras.Sequential([hub.KerasLayer(model_url)])
    #현재 5개의 데이터셋
    num_classes = 5
    bit_model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))

    return bit_model

def train_bit():

    #데이터 불러오기
    trainX, valX, trainY, valY = v1.split()

    #모델 불러오기
    bit_model = create_bit_model()
    
    
    #텐서플로우 파이프라인 사용하여 데이터셋 구성

    train_ds = tf.data.Dataset.from_tensor_slices((trainX, trainY)).batch(32)
    val_ds = tf.data.Dataset.from_tensor_slices((valX, valY)).batch(32)

    #모델 컴파일
    bit_model.compile(
        optimizer = tf.keras.optimizers.Adam(),
        loss = tf.keras.losses.SparseCategoricalCrossentropy(),
        metrics = [tf.keras.metrics.SparseCategoricalAccuracy()]
    )

    early_stopping = EarlyStopping(monitor='val_loss', patience=3)
    hist = bit_model.fit(train_ds, validation_data = val_ds, epochs=100, batch_size=32, callbacks=[early_stopping])
    bit_model.save('BigTransferModel.h5')

train_bit()


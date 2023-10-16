import tensorflow as tf
from keras import layers
from sklearn.model_selection import train_test_split
from keras import layers
import matplotlib.pyplot as plt
import preprocessing as pp

class CustomCnnModel(tf.keras.Model):
    """_summary_
    CNN 모델 선언 클래스
    Usage:
        모델을 인스턴스화하고 훈련 전에 컴파일을 진행
    """    
    def __init__(self):
        super(CustomCnnModel, self).__init__()

        self.conv1 = layers.Conv2D(64, (15, 15), activation='relu', input_shape=(256, 256, 3), padding='same', strides=(3, 3))
        self.conv2 = layers.Conv2D(64, (7, 7), activation='relu', padding='same', strides=(2, 2))
        self.conv3 = layers.Conv2D(32, (5, 5), activation='relu', padding='same')
        self.conv4 = layers.Conv2D(16, (3, 3), activation='relu', padding='same')

        self.batch_norm = layers.BatchNormalization()

        self.max_pool1 = layers.MaxPooling2D(pool_size=(3, 3))
        self.max_pool2 = layers.MaxPooling2D(pool_size=(2, 2))
        self.max_pool3 = layers.MaxPooling2D(pool_size=(2, 2))
        self.max_pool4 = layers.MaxPooling2D(pool_size=(2, 2))
        self.dropout = layers.Dropout(0.2)

        self.flatten = layers.Flatten()
        self.dense1 = layers.Dense(512, activation='relu')
        self.dense2 = layers.Dense(5, activation='softmax')

    def call(self, inputs):
        x = self.conv1(inputs)
        x = self.batch_norm(x)
        x = self.max_pool1(x)

        x = self.conv2(x)
        x = self.batch_norm(x)
        x = self.max_pool2(x)

        x = self.conv3(x)
        x = self.batch_norm(x)
        x = self.max_pool3(x)

        x = self.conv4(x)
        x = self.batch_norm(x)
        x = self.max_pool4(x)
        x = self.dropout(x)

        x = self.flatten(x)
        x = self.dense1(x)
        x = self.dense2(x)

        return x

#데이터 나누기
def split():
    """_summary_
    이미지와 라벨을 전처리 함수로 불러오고 train,test 데이터를 분리하는 함수
    Returns:
        list: 
            trainX (list): 훈련 이미지 데이터
            testX (list): 테스트 이미지 데이터
            trainY (list): 훈련 라벨 데이터
            testY (list): 테스트 라벨 데이터
    """    
    images,labels=pp.processing()
    trainX, testX, trainY, testY = train_test_split(images, labels, test_size=0.1, random_state=25, stratify = labels)
    trainX = trainX / 255
    testX = testX / 255 

    return trainX,testX,trainY,testY

#모델 훈련
def train():
    """_summary_
    모델 훈련 진행하여 모델을 저장하는 함수
    """    
    #모델 불러오기
    model = CustomCnnModel()

    #데이터 분리 / stratify를 사용하는 이유는 현재 두 개의 데이터셋의 개수가 균일하지 않기 때문 > 빅벤 100 언저리, 산토리니 400언저리
    trainX, testX, trainY, testY = split()

    #이미지 파일 > 정규화
    trainX = trainX / 255
    testX = testX / 255 

    #모델 컴파일 [sparse_categorical_crossentropy] : one-hot encoding 없이 정수 인코딩 된 상태에서 사용
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    hist1 = model.fit(trainX, trainY, epochs=20, batch_size=20)

    #모델 평가
    model.evaluate(testX, testY)

    plt.subplot(1,2,1)
    plt.plot(hist1.history['loss'])
    plt.subplot(1,2,2)
    plt.plot(hist1.history['accuracy'])
    plt.show()

    #모델 저장
    model_filename = 'train_model_v1.h5'
    model.save(model_filename)
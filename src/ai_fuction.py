from tensorflow import keras
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow_hub as tfhub
from src import test_ai
categories = {
    0: 'bigben',
    1: 'santorini',
    2: 'Matterhorn',
    3: 'Grand_Canyon',
    4: 'the_statue_of_liberty',
    5: 'eiffel_tower',
    6: 'Gold_gate_bridge',
    7: 'Osakajo',
    8: 'pisa_tower',
    9: 'ayasofya_camii',
    10: 'Donggung_Palace_and_Wolji_Pond',
    11: 'Gobi_Desert',
    12: 'Iceland_Aurora',
    13: 'kuta_beach',
    14: 'Machu_Picchu',
    15: 'Niagara_falls',
    16: 'Pyramid',
    17: 'Sydney_Opera_House',
    18: 'Torre_pendente_di_Pisa',
    19: 'Wat_Chedi_Luang'
}
class SingletonModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Singleton Instance")
            cls._instance = super(SingletonModel, cls).__new__(cls)

            # 모델 로딩 코드
            model_path = 'AI_MODEL/BigTransferModel1'
            with tf.keras.utils.custom_object_scope({'KerasLayer': hub.KerasLayer}):
                cls._instance.model = tf.keras.models.load_model(model_path, compile=False)
        return cls._instance

    def predict(self, processed_images):
        predictions = self.model.predict(processed_images)
        predicted_class_idx = np.argmax(predictions, axis=1)
        return predicted_class_idx
    



def numpy_to_image(imgs: object)-> object:
    """_summary_
    이미지를 입력받으면 넘파이 배열로 변환
    Args:
        imgs (object): 이미지 객체

    Returns:
        object: 이미지 객체
    """
    if isinstance(imgs, np.ndarray):
        # 첫 번째 차원이 1인 경우 제거
        if imgs.shape[0] == 1:
            imgs = np.squeeze(imgs, axis=0)
        
        # NumPy 배열을 PIL 이미지로 변환
        img = Image.fromarray(imgs)
        
        with BytesIO() as output:
            img.save(output, format="JPEG")
            return output.getvalue()

def preparing(images:list)->list:
    """_summary_
    넘파이 배열을 입력받으면 이미지의 사이즈를 조절하는 함수
    Args:
        images (list): 이미지

    Returns:
        list: 이미지
    """
    resized_images = []
    for img in images:
        pil_img = Image.fromarray(img)  # numpy 배열을 PIL Image로 변환
        resized_img = pil_img.resize((256, 256))  # 크기를 256x256으로 조절
        resized_images.append(np.array(resized_img))  # PIL Image를 numpy 배열

    imageArr = np.stack(resized_images, axis=0)
    imageArr = imageArr / 255.0
    return imageArr

def predicts(generated_images: object) -> object:
    
    singleton_model = SingletonModel()
    processed_images = preparing(generated_images)  # 이미지 전처리 함수
    
    predicted_results = []
    for img in processed_images:
        img_reshaped = np.expand_dims(img, axis=0)  # 모델이 받아들일 수 있는 형태로 차원을 추가
        if img_reshaped.shape[-1] != 3:  # 마지막 차원이 3이 아니면 채널을 추가
            img_reshaped = np.repeat(img_reshaped, 3, axis=-1)
        predicted_class_idx = singleton_model.predict(img_reshaped)
        predicted_results.append(categories[predicted_class_idx[0]])

    return predicted_results, generated_images


if __name__ == '__main__':
    inputText = input('텍스트 입력: ')
    text,imgs = predicts(test_ai.gan_generate(inputText))
    print(text)
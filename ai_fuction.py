from tensorflow import keras
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow_hub as tfhub


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
    image_list = [np.array(img) for img in images]
    imageArr = np.stack(image_list, axis=0)
    imageArr = imageArr / 255.0
    return imageArr

def predicts(generated_images: object)->object:
    """요약:
    이미지를 입력받으면 그이미지를 CNN모델에서 예측하는 함수
    
    Args:
        generated_images (object): 이미지 객체

    Returns:
        object: 예측된 결과 list와 이미지 객체
    """
    model_path = 'transfer_AI_MODEL/BigTransferModel1'
    with tf.keras.utils.custom_object_scope({'KerasLayer': hub.KerasLayer}):
        loaded_model = tf.keras.models.load_model(model_path,compile=False)

    processed_images = preparing(generated_images)
        

    predictions = loaded_model.predict(processed_images)
    predicted_class_idx = np.argmax(predictions, axis=1)
    img = numpy_to_image(generated_images)
    return categories[predicted_class_idx[0]], img

from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_hub as hub
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
# def test(path):
#     categories = {
#             0 : 'Bigben' ,
#             1 : 'Santorini',
#             2 : 'Matterhorn',
#             3 : 'Grand_Canyon',
#             4 : 'the_statue_of_liberty'

#         }
#     #모델 이름 입력
#     Mname = input('모델이름.h5 입력')

#     #모델 불러오기
#     with tf.keras.utils.custom_object_scope({'KerasLayer': hub.KerasLayer}):
#         loaded_model = tf.keras.models.load_model(Mname)
#     trainX,testX,trainY,testY = v1.split()

#     #테스트


#     #모델 예측 수행
    
#     pred = loaded_model.predict(testX)
    
#     test_image = keras.preprocessing.image.load_img(path, target_size=(256,256))
#     imageArr = np.array(test_image)
#     imageArr = imageArr / 255
#     imageArr = imageArr.reshape(-1,256,256,3)

#     pred = loaded_model.predict(imageArr)

#     pred_labels = np.argmax(pred, axis = 1)

#     #예측 결과 실행
#     print(categories[int(pred_labels)])
#     plt.title(categories[int(pred_labels)])
#     plt.imshow(imageArr[0])
#     plt.show()

def preparing(images:list)->list:
    image_list = [np.array(img) for img in images]
    imageArr = np.stack(image_list, axis=0)
    imageArr = imageArr / 255.0
    return imageArr

def val(generated_images, prompts):
    model_path = 'AI_train/BigTransferModel_v2.h5'
    with tf.keras.utils.custom_object_scope({'KerasLayer': hub.KerasLayer}):
        loaded_model = tf.keras.models.load_model(model_path,compile=False)
        

        
     
    processed_images = preparing(generated_images)
        
 
    predictions = loaded_model.predict(processed_images)
    predicted_class_idx = np.argmax(predictions, axis=1)
    
    return categories[predicted_class_idx[0]], generated_images,  
 
    # for i in range(images_to_generate):
    #     plt.figure(figsize=(10, 6))
    #     plt.imshow(processed_images[i])
    #     plt.title(f"Predicted Class: {categories[predicted_classes[i]]},{prompts}")
    #     plt.axis('off')
    # plt.show()
 

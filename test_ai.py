import keras_cv
import tensorflow as tf
import matplotlib.pyplot as plt
import keras
import matplotlib.pyplot as plt
from keras_cv.models import StableDiffusion
import translate as ts
import ai_fuction as af
## 모델은 개인이 다운로드 해야함!
def plot_images(images, title):
    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.title(title, fontsize=12)
        plt.axis("off")
    plt.show()
    
def gan_model():
    pass


# 1. 모델 로드
if __name__ == '__main__':
    img_height = img_width = 256
    model_path = 'ai_model/finetuned_stable_diffusion_gan_team.h5'
    gan_model = StableDiffusion(img_width=img_width, img_height=img_height)

# 2. 모델 사용
# 여기서는 예시로 'your_input_data'를 사용하였지만, 실제 입력 데이터로 변경해야 합니다.
# 만약 텍스트를 입력으로 사용한다면, 해당 텍스트를 적절한 형태로 전처리해야 합니다.
    gan_model.diffusion_model.load_weights(model_path)
    translator = ts.GoogleCloudTranslator('abstract-plane-396801-904742608cb2.json')
    test_to_translate = input('입력해라 : ')
    translated_text = translator.translate(test_to_translate, 'en')['tgt_text']
    prompts = translated_text
    images_to_generate = 1

    generated_images = gan_model.text_to_image(
        translated_text, batch_size=images_to_generate, unconditional_guidance_scale=40
    )
    af.val(generated_images, prompts, images_to_generate)

import keras_cv
import tensorflow as tf
import matplotlib.pyplot as plt
import keras
import matplotlib.pyplot as plt
from keras_cv.models import StableDiffusion
import translate as ts
import ai_fuction as af

## 모델은 개인이 다운로드 해야함!
def gan_model(translated_text):
    img_height = img_width = 256
    model_path = 'ai_model/finetuned_stable_diffusion_gan_team.h5'
    gan_model = StableDiffusion(img_width=img_width, img_height=img_height)
    gan_model.diffusion_model.load_weights(model_path)
    images_to_generate = 1
    generated_images = gan_model.text_to_image(
        translated_text, batch_size=images_to_generate, unconditional_guidance_scale=70
    )
    return generated_images

# 1. 모델 로드
if __name__ == '__main__':
    img_height = img_width = 256
    model_path = 'ai_model/finetuned_stable_diffusion_gan_team.h5'
    gan_model = StableDiffusion(img_width=img_width, img_height=img_height)

    gan_model.diffusion_model.load_weights(model_path)
    translator = ts.GoogleCloudTranslator('abstract-plane-396801-904742608cb2.json')
    test_to_translate = input('입력해라 : ')
    translated_text = translator.translate(test_to_translate, 'en')['tgt_text']
    prompts = translated_text
    images_to_generate = 1

    generated_images = gan_model.text_to_image(
        translated_text, batch_size=images_to_generate,unconditional_guidance_scale=40)
    af.val(generated_images, prompts)

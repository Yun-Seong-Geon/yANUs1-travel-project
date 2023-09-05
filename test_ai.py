import keras
from keras_cv.models import StableDiffusion
import translate as ts
import ai_fuction as af


# 모델은 개인이 다운로드 해야함!
def gan_model(translated_text: str)-> any:
    """_summary_

    Args:
        translated_text (str): 번역되어있는 문장을 입력받으면 이미지를 생성

    Returns:
        any: 생성된 이미지를 출력함
    """
    img_height = img_width = 256
    model_path = 'ai_model/finetuned_stable_diffusion_gan_team.h5'
    gan_model = StableDiffusion(img_width=img_width, img_height=img_height)
    gan_model.diffusion_model.load_weights(model_path)
    images_to_generate = 1
    generated_images = gan_model.text_to_image(
        translated_text,
        batch_size=images_to_generate,
        unconditional_guidance_scale=70
    )
    return generated_images


# 1. 모델 로드
if __name__ == '__main__':
    img_height = img_width = 256
    # model_path = 'ai_model/finetuned_stable_diffusion_gan_team.h5'
    keras.mixed_precision.set_globa_policy('mixed_float16')
    gan_models = StableDiffusion(img_width=img_width, img_height=img_height, jit_compile=True)

    # gan_model.diffusion_model.load_weights(model_path)
    translator = ts.GoogleCloudTranslator(
        'abstract-plane-396801-904742608cb2.json')
    test_to_translate = input('입력해라 : ')
    translated_text = translator.translate(test_to_translate, 'en')['tgt_text']
    prompts = translated_text
    images_to_generate = 1

    generated_images = gan_models.text_to_image(
        translated_text,
        num_step=50,
        batch_size=images_to_generate,
        unconditional_guidance_scale=7.5,
        temperature=1)
    af.val(generated_images)

from keras_cv.models import StableDiffusion


# 모델은 개인이 다운로드 해야함!
def gan_model(translated_text: str)-> any:
    """_summary_
    영어로 된 문장을 입력받으면 이에 맞게 GAN모델이 실행되며 
    이미지를 출력하는 함수
    Args:
        translated_text (str):

    Returns:
        any: 생성된 이미지를 출력함
    """
    img_height = img_width = 512
    gan_model = StableDiffusion(img_width=img_width, img_height=img_height,jit_compile=True)
    images_to_generate = 3
    generated_images = gan_model.text_to_image(
        translated_text,
        batch_size=images_to_generate,
        unconditional_guidance_scale=45
    )
    return generated_images



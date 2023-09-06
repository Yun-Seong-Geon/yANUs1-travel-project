#pip install googletrans==4.0.0rc1
# 번역 구글 api 추가 실행
#pip install --upgrade google-cloud-translate
from googletrans import Translator
from google.cloud import translate_v2 as translate
from google.oauth2.credentials import Credentials
from google.auth.exceptions import DefaultCredentialsError

class GoogleCloudTranslator:
    def __init__(self, credentials_path: str):
        """_summary_
            구글클라우드 번역기 api 생성자
        Args:
            credentials_path (str): 패스경로
        """
        self.client = translate.Client.from_service_account_json(credentials_path)
        self.result = {'src_text': '', 'src_lang': '', 'tgt_text': '', 'tgt_lang': ''}

    def translate(self, text: str, lang='en') -> dict:
        """_summary_

        Args:
            text (str): 번역할 텍스트
            lang (str, optional): _description_. Defaults to 'en'. 영어가 기본

        Returns:
            dict: _description_
        """
        translated = self.client.translate(text, target_language=lang)

        self.result['src_text'] = text
        self.result['src_lang'] = translated['detectedSourceLanguage']
        self.result['tgt_text'] = translated['translatedText']
        self.result['tgt_lang'] = lang

        return self.result
## 사용 예시   
if __name__ == '__main__':
    translator = GoogleCloudTranslator('abstract-plane-396801-904742608cb2.json')
    test_to_translate = input('입력해라 : ')
    translated_text = translator.translate(test_to_translate, 'en')['tgt_text']
    print(translated_text)


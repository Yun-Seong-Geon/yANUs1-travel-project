#pip install googletrans==4.0.0rc1
#pip install --upgrade google-cloud-translate
from googletrans import Translator
from google.cloud import translate_v2 as translate
from google.oauth2.credentials import Credentials

class GoogleCloudTranslator:
    def __init__(self, credentials_path: str):
        creds = Credentials.from_authorized_user_file(credentials_path)
        self.client = translate.Client(credentials=creds)
        self.result = {'src_text': '', 'src_lang': '', 'tgt_text': '', 'tgt_lang': ''}

    def translate(self, text: str, lang='en') -> dict:
        translated = self.client.translate(text, target_language=lang)

        self.result['src_text'] = text
        self.result['src_lang'] = translated['detectedSourceLanguage']
        self.result['tgt_text'] = translated['translatedText']
        self.result['tgt_lang'] = lang

        return self.result

# 사용 예시:



    
    
    ## 파이썬 번역 프로그램 
# if __name__ == '__main__':
#     translator = Google_Translator()
#     print(translate_eng('안녕하세요!!'))
 
#     # Select the language you want to translate to
#     tgt_lang_code = input('# Enter language code (Default: en): ')
 
#     if tgt_lang_code == '':
#         tgt_lang_code = 'en'
 
#     print('>> You chose: {}\n'.format(tgt_lang_code))
 
#     # Select the option you want to use
#     input_message = '# Pick an option: text or file: \n'
 
#     for index, option in enumerate(options):
#         input_message += f'{index + 1}. {option}\n'
    
#     input_message += 'Enter your choice: '
 
#     option = input(input_message)
    
#     print('>> You chose: {}\n'.format(options[int(option) - 1]))
 
#     # Translate the text
#     if option == '1':
#         input_text = input('Press Enter to translate: ')
#         result = translator.translate(input_text, tgt_lang_code)
 
#         print('[{}] -> [{}]'.format(result['src_lang'], result['tgt_lang']))
#         print('=' * 50)
#         print('Source Text : {}'.format(result['src_text']))
#         print('Target Text : {}'.format(result['tgt_text']))
#     # Translate the file
#     elif option == '2':
#         file_path = input('Enter file path: ')
#         result = translator.translate_file(file_path, tgt_lang_code)
 
#         print('[{}] -> [{}]'.format(result['src_lang'], result['tgt_lang']))
#         print('=' * 50)
#         print('Source Text : [{}]\n'.format(result['src_text']))
#         print('Target Text : [{}]'.format(result['tgt_text']))
#pip install googletrans==4.0.0rc1
from googletrans import Translator

options = ['text', 'file']
class Google_Translator:
    def __init__(self):
        self.translator = Translator()
        self.result = {'src_text': '', 'src_lang': '', 'tgt_text': '', 'tgt_lang': ''}
 
    def translate(self, text, lang='en'):
        translated = self.translator.translate(text, dest=lang)
        self.result['src_text'] = translated.origin
        self.result['src_lang'] = translated.src
        self.result['tgt_text'] = translated.text
        self.result['tgt_lang'] = translated.dest
 
        return self.result

    
def translate_eng(text):
    translator = Google_Translator()
    result = translator.translate(text,'en')
    
    return result['tgt_text']
        
    
    
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
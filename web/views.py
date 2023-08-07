from flask import Blueprint
from flask import Flask,render_template
from flask_login import login_required,current_user
import translate as ts
from flask import request,flash,redirect,url_for
from functools import wraps

views = Blueprint('view',__name__)

@views.route("/")
def home():
    return render_template('login.html')


@views.route('/main', methods=['GET', 'POST'])
@login_required
def main():
    user_nickname = current_user.nickname
    translated_text = ""
    if request.method == 'POST':
        text_to_translate = request.form.get('trans_text')
        if text_to_translate is None or text_to_translate.strip() == "":
            flash('텍스트를 입력해주세요.', category='error')
        else:
            translator = ts.Google_Translator()
            translated_text = translator.translate(text_to_translate, 'en')['tgt_text']
    return render_template('main.html', translated_text=translated_text,user_nickname=user_nickname)
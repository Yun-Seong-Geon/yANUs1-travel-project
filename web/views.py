from flask import Blueprint,session,jsonify
from flask import Flask,render_template
from flask_login import login_required,current_user
import translate as ts
from flask import request,flash,redirect,url_for
from functools import wraps
import test_ai as ai
import ai_fuction as af
import base64
from io import BytesIO
from PIL import Image
import numpy as np
translate_json_path = 'abstract-plane-396801-904742608cb2.json'
views = Blueprint('view',__name__)

@views.route("/")
def home():
    return render_template('login.html')
@views.route("/main/mypage")
def mypage():
    user_nickname = current_user.nickname
    return render_template('mypage.html',user_nickname=user_nickname)

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
            translator = ts.GoogleCloudTranslator(translate_json_path)
            translated_text = translator.translate(text_to_translate, 'en')['tgt_text']
            session['translated_text'] = translated_text
            return redirect(url_for('view.result',search = translated_text))
    return render_template('main.html',user_nickname=user_nickname,translated_text=translated_text)

@views.route('/result')
@login_required
def result():
    search_term = request.args.get('search', default="")
    # translated_text = session.get('translated_text', "")
    if not search_term:
         # 검색어가 쿼리 파라미터로 제공되지 않았다면 메인 페이지로 리디렉션
        return redirect(url_for('view.main'))
    translated_text = search_term
    a,b= af.val(ai.gan_model(translated_text),translated_text)
    if isinstance(b, np.ndarray):
        if b.shape[0] == 1:
            b = np.squeeze(b, axis=0)
        if b.shape[0] == 1:
            b = np.squeeze(b, axis=0)
    b = (b * 255).astype(np.uint8)
    b = Image.fromarray(b)
    buffered = BytesIO()
    b.save(buffered, format="JPEG")  # 0번째 이미지를 사용하는 것을 가정합니다.
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return render_template('result.html', img_cat = a,imgs = img_str, translated_text = search_term)


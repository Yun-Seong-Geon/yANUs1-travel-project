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
import time
from . import db
from werkzeug.security import check_password_hash
from .models import User,SearchHistory
translate_json_path = 'abstract-plane-396801-904742608cb2.json'
views = Blueprint('view',__name__)





@views.route("/")
def home():
    return render_template('login.html')





@views.route('/main/mypage', methods=['GET', 'POST'])
def mypage():
    if request.method == 'POST':
        # HTML 폼에서 제공된 데이터 가져오기
        nickname = request.form.get('gaib_nick')
        current_password = request.form.get('now_pw')
        new_password = request.form.get('gaib_pw')
        confirm_password = request.form.get('gaib_pw1')
        email = request.form.get('email')
        phone = request.form.get('phone')
        user = User.query.filter_by(id=current_user.id).first()
        # 예제: 닉네임 및 이메일 유효성 검사
        if not nickname or not email:
            flash("닉네임 및 이메일은 필수 입력 항목입니다.")
            return redirect(url_for('view.mypage'))
        
        if not check_password_hash(user.password,current_password):
            flash("비밀번호가 다릅니다.")
            return redirect(url_for('view.mypage'))
        
        # 새로운 비밀번호 확인
        if new_password != confirm_password:
            flash("비밀번호가 일치하지 않습니다.")
            return redirect(url_for('view.mypage'))

        # 데이터베이스 업데이트
        current_user.nickname = nickname
        if new_password:  # 새 비밀번호가 있을 경우만 업데이트
            current_user.password = new_password
        current_user.email = email
        current_user.phone = phone

        db.session.commit()
 
        flash("정보가 성공적으로 수정되었습니다.")
        return redirect(url_for('view.mypage'))

    user_nickname = current_user.nickname
    user_nickname = current_user.nickname
    search_history = SearchHistory.query.filter_by(user_id=current_user.id).order_by(SearchHistory.timestamp.desc()).all()
    return render_template('mypage.html', user_nickname=user_nickname,search_history=search_history)





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
            if text_to_translate:
            # 검색 기록 저장
                new_search = SearchHistory(user_id=current_user.id, search_text=text_to_translate)
                db.session.add(new_search)
                db.session.commit()
                
            translator = ts.GoogleCloudTranslator(translate_json_path)
            translated_text = translator.translate(text_to_translate, 'en')['tgt_text']
            session['translated_text'] = translated_text
            return redirect(url_for('view.result',search = translated_text))
    return render_template('main.html',user_nickname=user_nickname,translated_text=translated_text)




@views.route('/result')
@login_required
def result():
    search_term = request.args.get('search', default="")
    if not search_term:
        # 검색어가 쿼리 파라미터로 제공되지 않았다면 메인 페이지로 리디렉션
        return redirect(url_for('view.main'))
    return render_template('result.html', search_term=search_term)





@views.route('/get_prediction')
@login_required
def get_prediction():
    search_term = request.args.get('search', default="")
    translated_text = search_term
    img_cat, img_data = af.val(ai.gan_model(translated_text), translated_text)
    
    return jsonify({
        'translated_text': translated_text,
        'img_cat': img_cat,
        'img_src': img_data
    })


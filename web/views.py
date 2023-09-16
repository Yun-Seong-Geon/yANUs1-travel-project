from flask import Blueprint, session, jsonify, send_from_directory
from flask import render_template
from flask_login import login_required, current_user
from src import translate as ts
from flask import request, flash, redirect, url_for
from src import test_ai as ai
from src import ai_fuction as af
from src import scrap 
from . import db
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from .models import User, SearchHistory
import os

translate_json_path = 'abstract-plane-396801-904742608cb2.json'

views = Blueprint('view', __name__)


@views.route("/")
def home():
    return render_template('login.html')


@views.route('/main/mypage', methods=['GET', 'POST'])
def mypage()-> object:
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

        if not check_password_hash(user.password, current_password):
            flash("비밀번호가 다릅니다.")
            return redirect(url_for('view.mypage'))

        # 새로운 비밀번호 확인
        if new_password != confirm_password:
            flash("비밀번호가 일치하지 않습니다.")
            return redirect(url_for('view.mypage'))

        # 데이터베이스 업데이트
        current_user.nickname = nickname
        if new_password:  # 새 비밀번호가 있을 경우만 업데이트
            current_user.password = generate_password_hash(
                new_password, method='sha256')
        current_user.email = email
        current_user.phone = phone

        db.session.commit()

        flash("정보가 성공적으로 수정되었습니다.")
        return redirect(url_for('view.mypage'))

    user_nickname = current_user.nickname
    user_email = current_user.email
    user_id = current_user.id
    user_phone = current_user.phone
    search_history = SearchHistory.query.filter_by(user_id=current_user.id).order_by(
        SearchHistory.timestamp.desc()).limit(15).all()
    return render_template('mypage.html',user_id=user_id,user_email=user_email,user_phone=user_phone,user_nickname=user_nickname, search_history=search_history)


@views.route('/delete-history/<int:record_id>', methods=['DELETE'])
@login_required
def delete_history(record_id):
    record = SearchHistory.query.get(record_id)
    if not record:
        return jsonify({"message": "Record not found!"}), 404
    if record.user_id != current_user.id:
        return jsonify({"message": "Unauthorized!"}), 403

    db.session.delete(record)
    db.session.commit()
    return jsonify({"message": "Record deleted successfully!"}), 200


@views.route('/view-history-detail/<timestamp>')
def view_history_detail(timestamp):
    history_record = db.session.query(
        SearchHistory).filter_by(timestamp=timestamp).first()
    if not history_record:
        return "No record found for the given timestamp", 404
    history_record_img_path = history_record.image_path
    return render_template('history_detail.html',record=history_record,img_path=history_record_img_path)


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
                new_search = SearchHistory(user_id=current_user.id,search_text=text_to_translate)
                db.session.add(new_search)
                db.session.commit()
            tr = ts.GoogleCloudTranslator(translate_json_path)
            translated_text = tr.translate(text_to_translate, 'en')['tgt_text']
            session['translated_text'] = translated_text
            session['text_to_translate'] = text_to_translate
            return redirect(url_for('view.result',
                                    search=translated_text))
    return render_template('main.html',user_nickname=user_nickname,ranslated_text=translated_text)


@views.route('/result')
@login_required
def result():
    search_term = request.args.get('search', default="")
    if not search_term:
        # 검색어가 쿼리 파라미터로 제공되지 않았다면 메인 페이지로 리디렉션
        return redirect(url_for('view.main'))
    return render_template('result.html', search_term=search_term)


MEDIA_FOLDER = os.path.join('web/static/media')



@login_required
@views.route('/get_prediction')
def get_prediction():
    """_summary_
        이미지를 예측하는 함수
    Returns:
        _type_: json 파일
    """
    if not os.path.exists(MEDIA_FOLDER):  # Check if media directory exists
        os.makedirs(MEDIA_FOLDER)  # If not, create it

    search_term = request.args.get('search', default="")

    # 이미 예측된 값이 세션에 있으면 해당 값을 반환
    if 'predicted_data' in session and session['search_term'] == search_term:
        return jsonify(session['predicted_data'])

    # 예측 진행
    translated_text = search_term
    generated_images = ai.gan_generate(translated_text)  # Change this line

    img_cats = []
    img_srcs = []
    for idx, img_data_raw in enumerate(generated_images):  # Change this line
        img_cat, _ = af.predicts(img_data_raw)
        img_cats.append(img_cat)

        filename = secure_filename(f"{search_term}_{idx}.jpeg")
        image_path = os.path.join(MEDIA_FOLDER, filename)

        with open(image_path, 'wb') as f:
            f.write(img_data_raw)

        img_srcs.append(url_for('static', filename='media/' + filename))

    # 이미지 경로를 DB에 저장 (이 부분은 어떻게 처리할지에 따라 다를 수 있음)
    text_to_translate = session.get('text_to_translate')
    history = SearchHistory.query.filter_by(
        search_text=text_to_translate).first()
    if history:
        history.image_path = ','.join([secure_filename(f"{search_term}_{idx}.jpeg") for idx, _ in enumerate(generated_images)])  # Change this line
        db.session.commit()

    result = {
        'translated_text': translated_text,
        'img_cats': img_cats,
        'img_srcs': img_srcs
    }

    # 예측 결과와 검색어를 세션에 저장
    session['predicted_data'] = result
    session['search_term'] = search_term

    return jsonify(result)



@views.route('/media/<filename>')
def media_serve(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

@views.route('/information')

def information():
    search_term = request.args.get('search', default="")
    text_to_translate = session.get('text_to_translate')
    스크랩결과 = scrap.scrap_tourist_site_info(text_to_translate)
    
    return render_template('information.html', search_term = search_term, scrap_source = 스크랩결과)

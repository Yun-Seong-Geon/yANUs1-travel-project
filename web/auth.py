from flask import Blueprint,render_template,request,flash,redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
    
auth = Blueprint('auth', __name__)

@auth.route('/sign-in',methods=['GET','POST'])
def sign_in():
    if request.method == 'POST':
        id = request.form.get('login_id')
        password1 = request.form.get('login_pw')

        # search User in database & compare password
        user = User.query.filter_by(id=id).first()
        if user:
            if check_password_hash(user.password, password1):
                flash('로그인 완료', category='success')
                login_user(user, remember=True)
                return redirect(url_for('view.main'))
            else: 
                flash('비밀번호가 다릅니다.', category='error')
        else:
            flash('해당 아이디 정보가 없습니다.', category='error')

    return render_template('login.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('view.home'))



@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        # form - input의 name 속성을 기준으로 가져오기
        nickname = request.form.get('gaib_nick')
        email = request.form.get('email')
        gaib_id = request.form.get('gaib_id') # 이름 수정
        gaib_pw = request.form.get('gaib_pw') # 추가
        phone = request.form.get('phone') # 이름 수정
        
        # 중복 이메일 검사
        existing_user_email = User.query.filter_by(email=email).first()
        if existing_user_email:
            flash('이미 사용 중인 이메일입니다.', category='error')
            return render_template('gaib.html')

        # 중복 아이디 검사
        existing_user_id = User.query.filter_by(id=gaib_id).first()
        if existing_user_id:
            flash('이미 사용 중인 아이디입니다.', category='error')
            return render_template('gaib.html')

        # 중복 전화번호 검사
        existing_user_phone = User.query.filter_by(phone=phone).first()
        if existing_user_phone:
            flash('이미 사용 중인 전화번호입니다.', category='error')
            return render_template('gaib.html')
        
        # 중복 전화번호 검사
        existing_user_nick = User.query.filter_by(nickname=nickname).first()
        if existing_user_nick:
            flash('이미 사용 중인 닉네임 입니다.', category='error')
            return render_template('gaib.html')
        
        new_user = User(id = gaib_id ,
                        email=email, 
                        nickname=nickname, 
                        password=generate_password_hash(gaib_pw,method='sha256'),
                        phone = phone)
        db.session.add(new_user)
        db.session.commit()
        

        flash('회원가입 완료',category='success')
        return redirect(url_for('auth.sign_in'))
    return render_template('gaib.html')


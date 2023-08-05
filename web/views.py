from flask import Blueprint
from flask import Flask,render_template
from flask_login import login_required

views = Blueprint('view',__name__)

@views.route("/")
def home():
    return render_template('login.html')

@views.route('/main')
@login_required
def main():
    return render_template('main.html')
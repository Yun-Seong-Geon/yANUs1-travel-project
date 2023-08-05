from flask import Blueprint
from flask import Flask,render_template

views = Blueprint('view',__name__)

@views.route("/")
def home():
    return render_template('login.html')

@views.route("/login",methods=['GET','POST'])
def login():
    return render_template('login.html')
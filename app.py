from flask import Flask,render_template
import random
from web import create_app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,port=5001)
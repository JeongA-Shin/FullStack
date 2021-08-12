#-*- coding: utf-8 -*-

from flask import Flask,jsonify,request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/hello_if')
def hello_html():
    value = 27
    return render_template('condition.html', data=value) #data라는 변수에 value를 넣은 채로 condition.html을 띄움

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
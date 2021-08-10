from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hello/<user>') #라우팅 경로로 변수 값을 넣을 수 있음
def hello_name(user): #라우팅 경로의 변수값을 인자로 받음
    return render_template('variable.html', name1=user, name2=2) 
    #variable_html를 웹 브라우저로 띄우면서(당연히 variable.html 안에는 jinja 문법이 쓰임) - variable.html 참고
    #해당 html안의 name1은 user로(변수로),name2는 2로 적용하라


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")

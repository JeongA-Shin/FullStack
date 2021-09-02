from flask import Flask,jsonify,request
from flask.templating import render_template
#request는 url에 여러 파라미터 값들을 붙이기 위해 import함
#https://post.naver.com/viewer/postView.naver?volumeNo=32113292&memberNo=49649230&searchRank=51
#위의 url에서 volumeNo,memeberNo,searchRank 등이 url의 파라미터임
#당연히 각 파라미터(키)의 값은 32113292,49649230,51이 됨

app=Flask(__name__,static_url_path='/static') #객체, #모든 css 파일들은 static 폴더 안에 있음


@app.route('/login')
def login():
    #원래 login.html로 했을 때는 user_name, pw로 했다가 login_rawtest.html(부트스트랩의 예제)로 바꾸면서 email_address랑 passwd로 함
    #username=request.args.get('user_name')#http방식으로 주고받는 데이터(url의 파라미터로 표현됨) 중 user_name의 value를 username 변수에 담음
    #passwd = request.args.get('pw')
    email_address = request.args.get('email_address')
    passwd=request.args.get('passwd')
    print(email_address,passwd)

    if email_address=='dave@gmail.com': #url의 파라미터들의 해당 key의 값이 dave이면
        return_data={'auth':'success'}
    else:
        return_data={'auth':'failed'}
    return jsonify(return_data)


### flask 로 정적 웹페이지 로드하기 
# 프론트엔드 페이지도 flask 로 보여줄 수 있음
# flask render_template(HTML파일명): HTML 파일 전송하기
# 제일 중요!!!!!! HTML파일은 flask 가 실행되는 하위 폴더인 templates 폴더 안에 위치해야 함
@app.route('/html_test')
def hello_html():
    return render_template('login_rawtest.html') #rener_template('html명')을 통해서 해당 html을(template 폴더 안의) 브라우저에 띄우는 것
#즉 내가 해당 단락의 코드를 추가함으로서 go live로 띄우지 않아도 http://192.168.123.195:8080/html_test로 들어가면 
# templates 폴더 안에 있는 login.html이 뜨고
#거기서 내가 아이디와 패스워드를 넣고 submit을 하면 위에서 json처리한 결과가 나타난다!
#즉 이 코드로 go live가 아니라(go live 대신ㄴ에) 완전히 flask로만 한 것!


if __name__=='__main__':
    app.run(host='192.168.123.195',port="8080",debug=True)

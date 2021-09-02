#메인서버 - blog.py등을 돌리기 위한 웹서버. 서버 객체(app)을 만들고 돌림
from flask import Flask,jsonify,request,render_template,make_response,session
#request는 argument 등을 가지고 처리해야하므로 
#render_template은 html페이지를 리턴할 때
#make_response는 status code까지 넘겨주기 위한 것
from flask_login import LoginManager,current_user,login_required,login_user,logout_user
#Login_Manager를 통해 session 관리를 해줌
#current_user는 로그인 정보!!를 객체로! 처리할 수 있음
#login_required는 로그인을 한 사용자만 접근할 수 있는 api를 만들어줄 때 사용
#login_user를 통해서 로그인을 하면 해당 객체를 user객체로 넘겨주어서 session이 만들어지고 그 외 구성을 해줌
#logout_user는 로그아웃을 할 때는 해당 객체를 logout_user에 넘겨주기만 하면 됨
from flask_cors import CORS
#서로 다른 웹 서버 상에서의 데이터 요청/교환(스크립트 기반)을 위한 것
from blog_view import blog #내가 만든 blog_view 폴더에서 내가 만든 blog.py를 import한 것
from blog_control.user_mgmt import User  #내가 만든 blog_control 폴더의 user_mgmt.py에서 내가 만든 User class를 import한 것

import os #보안 로그인 예:http로만 하다가 https로 바꿔줌


# https에서만을 지원하는 기능을 http 에서 테스트할 때 필요한 환경설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

#서버 만들기
app=Flask(__name__,static_url_path='/static') #현재 서버가 띄울 html파일에 관련된 정보는 static 폴더 안에 있다
CORS(app) #서로 다른 서버간의 지원을 가능하게 하기 위해
app.secret_key='jeong_server1'#flask 로그인을 위한 키. 
#보안을 위해서 껐다 켤 때마다 다르게 설정해버리면 그 때마다 session정보가 모두 날라가므로 그냥 지정함
#secret_key가 있어야 flask에서 http request를 기반으로 세션 정보를 생성 가능

#blue print 등록 - 여기서 blog.py에서 설정한 라우팅 경로들이 웹 서버를 통해서 동작할 수 있게 됨
app.register_blueprint(blog.blog_abtest,url_prefix='/blog') # blog_view 폴더의 blog.py에서 생성한 객체 이름이 blog_abtest임

#플라스크 로그인 지원
login_manager=LoginManager()
login_manager.init_app(app)#로그인 매니저에 app(내가 쓸 서버,플라스크 객체)을 등록시킴
login_manager.session_protection='strong' #이렇게 해줘야 세션을 보다 복잡하게 만듦(보안성 높음)!!


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) #해당 id를 가지고 mysql에서 해당 id에 해당하는 레코드를 가져와서 객체로 리턴함
#즉 flask login은 누군가 사용자 객체를 만들어서 로그인을 하면 세션 관리를 해주고, 
# 요청에 세션 정보가 포함되어 있으면 세션 정보에서 id기반으로 객체를 만들기 위해 이 함수를 호출함

@login_manager.unauthorized_handler
def Unauthorized():
    return make_response(jsonify(success=False),401)
#로그인이 안 된 사용자가 로그인이 된 사용자만 접근할 수 있는 api들을 요청했을 경우에 이 함수가 호출됨
#즉 로그인이 안 된 사용자가 로그인이 필요한 기능들에 접근할 수 없게 함


@app.before_request
def app_before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get( #session은 사전처럼 처리 가능
            'HTTP_X_REAL_IP', request.remote_addr) #즉 session의 client_id에 ip주소를 저장하는 것


if __name__=='__main__':
    app.run(host='0.0.0.0',port='8080',debug=True)

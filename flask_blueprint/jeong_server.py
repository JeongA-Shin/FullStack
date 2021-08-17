# 메인서버
from flask import Flask
from sub_blueprint import blog_test

app = Flask(__name__)
app.register_blueprint(blog_test.blog_ab, url_prefix='/blog') #메인서버에서, /blog로 들어가는 것을 blueprint로 한다고 등록을 하는 것임!
# /blog로 들어가는 웹페이지들을 app에 blueprint로 등록
#blog_ab는 blog_test 파일에 선언되어 있음

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')

#즉, 기능별로 서브 폴더들을 만들어 두고
#각 서브 폴더 안의 파일에서 각각 blue print 객체를 생성한 다음에
#그 boueprint 객체들을 메인서버의 app 객체에 등록하는 것이다.
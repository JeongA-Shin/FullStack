'''
Controller
사용자가 접근 한 URL에 따라서 사용자의 요청사항을 파악한 후에 
그 요청에 맞는 데이터를 Model에 의뢰하고, 데이터를 View에 반영해서 사용자에게 알려준다. 

Model
일반적으로 CI의 모델은 데이터베이스 테이블에 대응된다. 

View

View는 클라이언트 측 기술인 html/css/javascript들을 모아둔 컨테이너이다. 
'''

from db_model.mongodb import conn_mongodb #내가 만든 db_model.mongodb 폴더의 mongodb.py에서 conn_mongodb 함수만 가져옴
from datetime import datetime #access시간을 알기 위해서


class BlogSession(): #상속 필요 없음
    blog_page={'A':'blog_A.html','B':'blog_B.html'}
    session_count=0 #클래스 변수

    #접속할 때마다 접속 정보를 mongoDB에 저장(컬렉션을 생성)하는 함수
    #staticmethod에 대한 설명은 python_class폴더에 있음
    @staticmethod
    def save_session_info(session_ip,user_email,webpage_name):
        now=datetime.now() #지금 현재 시간
        now_time = now.strftime("%d/%m/%Y %H:%M:%S") #현재 시간(now에 있음)을 str로 바꿈 
        mongo_db=conn_mongodb()
        mongo_db.insert_one({
            'session_ip':session_ip,
            'user_email':user_email,
            'page':webpage_name,
            'access_time':now_time
        })


    @staticmethod
    def get_blog_page(blog_id=None): #인자를 넣지 않아도 되고 만약 인자가 있다면 해당 인자를 쓸 수 있게끔
        #blog_A.html과 blog_B.html이 접속할 때마다 번갈아 나오도록 함
        if blog_id == None:
            if BlogSession.session_count==0:
                BlogSession.session_count=1
                return BlogSession.blog_page['A']
            else:
                BlogSession.session_count=0
                return BlogSession.blog_page['B']
        else:
            #BlogSession.save_session_info(session)
            return BlogSession.blog_page[blog_id]

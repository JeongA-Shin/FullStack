from flask_login import UserMixn
'''
Flask 로그인에는 다음 속성을 가진 사용자 모델이 필요합니다.

사용자가 유효한 자격 증명을 제공한 경우 True를 반환하는 is_authenticated() 메서드가 있습니다.
사용자의 계정이 활성 상태이면 True를 반환하는 is_active() 메서드가 있습니다.
현재 사용자가 익명 사용자인 경우 True를 반환하는 is_anonymous() 메서드가 있습니다.
사용자 인스턴스가 주어지면 해당 객체의 고유 ID를 반환하는 get_id() 메서드가 있습니다.

!!!!!!!!!! UserMixin 클래스는 이 속성의 구현을 제공합니다.!!!!!!!!

예: is_authenticated를 들어 로그인 자격 증명이 제공하는 것이 올바른지 확인하기 위해 직접 메소드를 작성하는 대신 호출할 수 있는 이유 입니다.

'''
from db_model.mysql import conn_mysql #내가 만든 db_model 폴더 안의 mysql.py 안에 conn_mysql이라는 함수만 가져옴

class User(UserMixn): #user 클래스가 usermixn을 상속받음
    def __init__(self,user_id,user_email,blog_id): #생성자
        self.id= user_id
        self.user_email=user_email
        self.blog_id=blog_id

    def get_id(self):
        return str(self.id)

    #db에서 user_id로만 해당되는 레코드 정보를 뽑아내는 함수
    @staticmethod #정적 메서드에 대한 설명은 python_class 폴더 안에 있음
    def get(user_id): #db에서 해당 유저에 대한 레코드를 뽑음
        mysql_db=conn_mysql() #연결된 객체
        db_cursor=mysql_db.cursor() # 연결된 것을 가르키는 커서
        sql="SELECT * FROM user_info WHERE USER_ID='"+str(user_id)+"'"
        db_cursor.execute(sql)
        user=db_cursor.fetchone() #어차피 해당되는 유저는 한 명일테니까 그냥 fetchone을 함
        if not user: #해당되는 게 없다면 바로 종료
            return None
        #해당되는 게 있다면
        user=User(user_id=user[0],user_email=user[1],blog_id=user[2])


    #db에서 user_email로만 해당되는 레코드 정보를 뽑아내는 함수 - 위의 get함수와 거의 비슷함
    @staticmethod
    def find(user_email):
        mysql_db=conn_mysql() #연결된 객체
        db_cursor=mysql_db.cursor() # 연결된 것을 가르키는 커서
        sql="SELECT * FROM user_info WHERE USER_EMAIL='"+str(user_email)+"'"
        db_cursor.execute(sql)
        user=db_cursor.fetchone() #어차피 해당되는 유저는 한 명일테니까 그냥 fetchone을 함
        if not user: #해당되는 게 없다면 바로 종료
            return None
        #해당되는 게 있다면
        user=User(user_id=user[0],user_email=user[1],blog_id=user[2])


    #user 데이터를 넣는 함수 -  이메일이 중복되지 않도록
    @staticmethod
    def create(user_email,blog_id):
        user=User.find(user_email)  #일단 한 번 찾아보고
        if user == None: #없으면
            mysql_db=conn_mysql() #연결된 객체
            db_cursor=mysql_db.cursor() # 연결된 것을 가르키는 커서
            sql="INSERT INTO user_info (USER_EMAIL,BLOG_ID) VALUES (%s,%s)" % (str(user_email),str(blog_id))
            db_cursor.execute(sql)
            mysql_db.commit() #완전히 반영
            return User.find(user_email) #추가된 그 레코드 객체를 반환
        else: #이미 있었으면
            return user

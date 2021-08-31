import pymongo
from pymongo.mongo_client import MongoClient

MONGO_HOST='localhost'#사용자가 아니라!db가 돌아가는 서버를 가르키는 것
MONGO_CONN=pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))

def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster') #연결되었는지 확인 시도
        blog_ab=MONGO_CONN.blog_session_db.blog_ab #만약 연결되었으면 blog_session이라는 db에 blog_ab라는 컬렉션을 생성함
    except:
        MONGO_CONN=pymongo.MongoClient('mongodb://%s' % (MONGO_HOST)) #만약 try가 에러나면 다시 연결 시도해서 
        blog_ab=MONGO_CONN.blog_session_db.blog_ab #다시 blog_session이라는 db에 blog_ab라는 컬렉션을 생성 시도
    return blog_ab #내가 생성한 컬렉션을 리턴하도록 함
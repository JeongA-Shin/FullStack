import pymongo

username = ''
password = ''
ip_address = 'localhost'
connection = pymongo.MongoClient()
connection = pymongo.MongoClient('mongodb://%s' % (ip_address))
'''
이 과정을 아래 conn_mongodb()로 만들어 낸 것
# connection = pymongo.MongoClient('mongodb://%s:%s@%s' % (username, password, ip_address))
blog_session_db = connection.blog_session_db #없으면 만들어짐
blog_ab = blog_session_db.blog_ab


#print(connection.admin.command('ismaster')) #연결되었는지 확인'''


def conn_mongodb():
    try:
        connection.admin.command('ismaster') #연결되었으면
        blog_ab = connection.blog_session_db.blog_ab
    except: #연결 확인이 안 되면
        connection = pymongo.MongoClient('mongodb://%s' % (ip_address)) 
        blog_ab = connection.blog_session_db.blog_ab

    return blog_ab
import pymysql

MYSQL_HOST='localhost' #사용자랑 다름. db가 돌아갈 서버를 뜻하는 거임
MYSQL_CONN=pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='root',
    passwd='anjfgkfksmsakfdldi0613!',
    db='blog_db',
    charset='utf8'
)


def conn_mysql():
    if not MYSQL_CONN.open: #만약 끊어진 경우
        MYSQL_CONN.ping(reconnect=True) #이 구문을 통해 재접속 가능

    return MYSQL_CONN #연결된 "객체"를 리턴함
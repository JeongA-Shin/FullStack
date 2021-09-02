import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='root',
    passwd='anjfgkfksmsakfdldi0613!',
    db='blog_db',
    charset='utf8')


def conn_mysqldb():
    if not MYSQL_CONN.open: #열리지 않으면
        MYSQL_CONN.ping(reconnect=True) #ping은 네트워크 상태를 점검하는 명령어 #즉, 열리지 않으면 재접속하라
    return MYSQL_CONN

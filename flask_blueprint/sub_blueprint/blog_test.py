# blog_test.py
from flask import Blueprint

blog_ab = Blueprint('blog', __name__) #blog_ab가 객체인 거임. /blog로 들어가는 모든 라우팅 경로는 blog_ab.route로 설정

# http://localhost:8080/blog/blog1
@blog_ab.route('/blog1')
def blog():
    return 'TEST BLUEPRINT'

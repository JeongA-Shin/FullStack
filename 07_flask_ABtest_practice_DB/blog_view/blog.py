from flask import Flask,Blueprint,request,render_template,make_response,redirect,url_for
#redirect는 return을 다른 라우팅 경로로 해주게끔 함- 단 경로를 풀로 다 써줘야 함

from flask.json import jsonify

#blog.py는 각종 기능들을 연결해주고, 각종 라우팅 경로들을 설정해줌
#ex) submit버튼을 누르면 어느 페이지로 라우팅되는지

blog_abtest=Blueprint('blog',__name__)


@blog_abtest.route('/set_email',methods=['GET','POST'])#GET과 POST방식 모두 지원한다는 의미
def set_email(): #라우팅 경로와 똑같이 함수명을 해주어야 헷갈리지 않음
    #get방식인 경우
    if request.method=="GET": 
        print(request.args.get('user_email')) #그냥 이렇게 끝내면 return이 없어서 웹 페이지가 보여줄 게 없어서 에러남. 
        #그래서 make_reponse결과를 리턴해줌
        #return make_response(jsonify(success=True),200)
        #return redirect('/blog/test_blog')
        return redirect(url_for('blog.test_blog')) #url_for을 써주면 blueprint,해당 함수명를 좀 더 직관적으로 확인할 수 있다는 장점
        #그냥 redirect만 써도 상관 없음!
        #url_for(blueprint.함수명) #url_for은 라우팅경로가 아니라! 함수명자체를 써주는 거임!
    #post인 경우
    else:
        #print(request.headers) #이걸로 확인해보면 Content-Type: application/x-www-form-urlencoded임
        #print(request.get_json()) #request.get_json()으로 body 정보를 가져오려면 application/json이어야 함 
        #그래서 그냥 None이 나옴 . 그런데 우리는 대부분 form을 통해 data를 요청하고 가져옴 따라서
        #print(request.form) #ImmutableMultiDict([('user_email', 'hello@khu.ac.kr'), ('blog_id', 'A')]) #[('키','값'),('키','값')]
        print(request.form['user_email']) #hello@khu.ac.kr
        return redirect(url_for('blog.test_blog'))

    
    
@blog_abtest.route('/test_blog')
def test_blog():
    return render_template('blog_A.html')
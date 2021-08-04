from flask import Flask  #flask 라이브러리 중 FLASK 클래스만 필요함

#만들고자하는 웹 서비스에 해당되는 객체를 하나 만듦

#app=Flask(__name__)   #그리고 그 객체에 웹 서비스의 기능들이 하나씩 추가됨
#print(__name__)       #__main__ #현재 이 코드 내에서 실행되는 것이므로 __main__ 값이 들어감
#print(app)            #<Flask 'flask_basic'> #app자체를 프린트하면 현재 실행되는 게 어떤 기능(어떤 파일)인지 알 수 있음

'''
__name__이라는 변수는 import된 모듈의 이름이 저장되고,
만약 import한 모듈이 없거나, 현재의 코드에 __name__이 있으면
__main__이라는 값이 들어감

즉! __name__의 필요성: 모듈로서 실행할지, 해당 코드 직접 실행시에만 실행할지를 결정할 수 있음

if __name__ == "__main__"을 사용하면
직접 이 파일을 실행했을 때는 __name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다.
반대로 다른 파일에서 이 모듈을 불러서 사용할 때는 __name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.
(점프 투 파이썬 설명 참고)
'''

'''#라우팅 경로 설정
#라우팅이란 적절한 목적지를 찾아주는 기능
#url을 찾는 기능과 연결해줌
#@웹객체이름.route("/찾는경로") #반드시 /로 시작해야함!

#예: http://www.fun-coding.org/hello이면
@app.route("/hello") #http://www.fun-coding.org 서버에서 hello라는 목적지에 맞는 <<<함수를 호출해줌>>>
def hello():  #함수명은 경로명과 달라도 됨
    return "<h1>Hello Wrold</h1>"
#@로 시작하는 코드는 데코레이터라고 함'''

#flask의 웹서버
##메인 모듈로 실행될 때, flask의 자체 웹 서버 구동
#app.run으로 서버 구동 가능(host-웹 주소,port-포트 번호,debug-True or False주로 사용)


'''#기본 개발 프로세스
host_addr="0.0.0.0"         #localhost,127.0.0.1,0.0.0.0 등으로 host 설정
port_num="8080"

if __name__=="__main__":
    app.run(host=host_addr,port=port_num,debug=True)'''


####전체 기본 코드 - 위의 기본 내용들 모두 합친 것####
##실행하면 현재  * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit) 이런 내용이 뜸
#우선 웹 서비스를 나타내는 앱 객체를 만들어줌
app=Flask(__name__)
#/hello로 들어가면 <h1>Hello Flask</h1>를 띄워라
@app.route("/hello")
def hello():
    return "<h1>Hello Flask</h1>" 

#현재 코드를 실행하는 거라면 웹 서버를 띄워라
if __name__=="__main__":
    app.run(host="127.0.0.1",port="8080",debug=True)
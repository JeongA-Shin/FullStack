from flask import Flask
## 3. flask 와 Rest API

app = Flask(__name__)


def add_file(data):
    return data + 5

@app.route("/")
def hello():                           
    return "<h1>Hello World!</h1>"

@app.route("/profile/<username>")
def get_profile(username):
    return "profile: " + username

@app.route("/first/<username>")
def get_first(username):
    return "<h3>Hello " + username + "!</h3>"


@app.route("/message/<int:message_id>")
def get_message(message_id):
    return "message id: %d" % message_id   # %d 는 int, %f 는 float, %s 는 string

@app.route("/first/<int:messageid>")
def get_first(messageid):
    data = add_file(messageid)
    return "<h1>%d</h1>" % (data)



if __name__ == "__main__": #현재의 코드를 코드로서! 직접 실행시키는 중이면 웹 서버를 구동시켜라             
    app.run(host="0.0.0.0", port="8080",debug=True)


'''#REST_API에 대해서
### REST
- REST(REpresentational State Transfer)
  - 자원(resource)의 표현(representation)에 의한 상태 전달
  - HTTP URI를 통해 자원을 명시하고, HTTP Method를 통해 자원에 대한 CRUD Operation 적용
    - CRUD Operation와 HTTP Method
      - Create: 생성 (POST)
      - Read: 조회 (GET)
      - Update: 수정 (PUT)
      - Delete: 삭제 (DELETE)

### REST API
- REST 기반으로 서비스 API를 구현한 것
- 마이크로 서비스, OpenAPI(누구나 사용하도록 공개된 API) 등에서 많이 사용됨'''

'''### flask 로 REST API 구현 방법
- 특정한 URI를 요청하면 <JSON 형식>으로 데이터를 반환하도록 만들면 됨
- 즉, 웹주소(URI) 요청에 대한 응답(Response)를 JSON 형식으로 작성
- Flask에서는 dict(사전) 데이터를 응답 데이터로 만들고, 이를 jsonify() 메서드를 활용해서 JSON 응답 데이터로 만들 수 있음

### REST API 테스트를 위한 준비
### httpie 설치 -> postman으로 일일히 확인하기에는 시간이 많이 걸리니까 이거를 설치한다.+ 브라우저 페이지도 그냥 이걸로 확인할 수 있음
'''
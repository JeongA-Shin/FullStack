### REST API method 정의하기
from flask import Flask, request,make_response,jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app) #다른 서버에도 데이터 요청할 수 있도록 cors를 처리

# restapi_test.txt를 반드시!!!! 참고해서 읽은 후 코드 보기

@app.route("/test", methods=['GET', 'POST', 'PUT', 'DELETE']) # 파라미터에 따로  method를 넣지 않으면 디폴트로 get방식이 됨
def test():
    #함수에서 request를 import함. 그 request 덕에 http요청(url등을 통해)등을 분석해서 request.method라고 할 수 있는 것임
    if request.method == 'POST':
        print ('POST')
        data = request.get_json()  #post는 파라미터(ex.username, passwd등)와 그 값을 json형태로(딕셔너리) 전달함
        #get과는 다르게 파라미터들이 url로 전달이 되지 않으므로 이렇게 함
        print (data['email']) #그리고 내가 원하는 파라미터의 데이터을 key를 통해 value로 얻음,print는 터미널에서 확인 가능
    if request.method == 'GET':
        print ('GET')
        user = request.args.get('email') #get방식은 경우에는 post와 다르게 request.args.get()을 통해 직접적으로..?해당 파라미터의 값을 얻음
        #파라미터들이 url을 통해 바로 전달되므로 이렇게 함(보안에 상대적으로 취약)
        print (user)
    #put과 delete는 get처럼 동작하므로 동일하게 해주면 됨
    if request.method == 'PUT':
        print ('PUT')
        user = request.args.get('email')
        print (user)
    if request.method == 'DELETE':
        print ('DELETE')
        user = request.args.get('email')
        print (user)

    return make_response(jsonify({'status': 'success'}),200) #콘솔에서 확인할 수 있음(응답을)
    #그냥 return jsonify(success=True) 이렇게만 해도 되지만, 성공시 status_code=200임을 더 확실하게 넣기 위해서 make_response함수를 써줌

if __name__=='__main__':
    app.run(host="0.0.0.0",port="8082")
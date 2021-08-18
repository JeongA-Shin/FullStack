from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #flask 전체에 CORS를 적용(frontend_with_cors_and_restapi.txt 참고)- 그래야 서로 다른 서버끼리도 데이터 요청을 할 수 있음


@app.route("/test", methods=['GET'])
def test():
    return make_response(jsonify(success=True), 200) #console에 응답하는 거임 #html에서 script의 axios_test()함수 부분과 연동되는 것
    #그냥 return jsonify(success=True) 이렇게만 해도 되지만, 성공시 status_code=200임을 더 확실하게 넣기 위해서 make_response함수를 써줌


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8082")

#REST API에 대한 대략적인 설명은 4_flask_basic.py에 간략하게 설명해둠
#flask jsonify() 함수 - 리턴 데이터를 JSON 포맷으로 제공

from flask import Flask,jsonify
app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False #한글깨짐 방지



#data를 사전 데이터로 만들고, 이를 jsonify() 메서드에 넣어서 json형태로 리턴해주면 됨
@app.route('/json_test')
def hello_json():
    data={'name':'김대리','family':'Byu'}
    return jsonify(data) #이러면 json형태로 반환됨


@app.route('/server_info')
def server_json():
    data={'server_name':'0.0.0.0','server_port':'8080'}
    return jsonify(data)

if __name__=="__main__":
    app.run(host="0.0.0.0",port="8080",debug=True)






from flask import Flask 
import requests

app = Flask(__name__)   

#없는 페이지를 요청했을 때의 에러, errorhandler(status_code)
#errorhandler를 사용하여 HTTP 오류 코드가 나오는 페이지를 정의할 수 있음
#return 의 두번째 인자로 에러코드를 넘겨주지 않으면 200 성공으로 인지함
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Error</h1>", 404
    #render_template으로 해도 되고, 이렇게 직접 메세지를 써도 된다.
    #return 보이고자하는 페이지, 에러 코드(직접 설정 가능)

@app.route("/google")
def get_google():
    response = requests.get("http://www.google.co.kr")
    return response.text 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
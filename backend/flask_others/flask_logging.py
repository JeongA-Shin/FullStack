from flask import Flask
import requests

app = Flask(__name__)

'''## flask 와 logging
- logging 라이브러리와 함께 flask logging 기능 사용 가능
- 주요 logging 핸들러 (어떻게 로그를 다룰 것인지에 대해 미리 구현된 함수들을 제공)
 -즉 handler들의 종류
  - FileHandler - 파일로 로그를 저장
  - RotatingFileHandler -제일 많이 사용하는 handler, 파일로 로그를 저장하되 파일이 정해진 사이즈를 넘어가면 새로운 파일을 생성
    - maxBytes=하나의파일사이즈, backupCount=파일갯수
    - 전체 파일을 다 쓰면, 다시 처음부터 씀
  - NTEventLogHandler - 윈도우 시스템 로그로 남김
  - SysLogHandler - 유닉스 계열 시스템의 syslog 로 남김

 !!! 서버 상에서는 로그 파일이 전체 디스크를 채울 경우, 비정상동작을 할 수 있으므로 RotatingFileHandler 가 일반적인 경우에는 적합 '''

if not app.debug: #현재 아래의 서버 돌리는 걸 보면 debug가 false이므로 if문이 참이 되는 거임.(즉 debug를 안 하고 log를 진행한다는 것임)
    import logging
    from logging.handlers import RotatingFileHandler  # 내가 사용할 logging 핸들러를 import함
    file_handler = RotatingFileHandler('dave_server.log', maxBytes=2000, backupCount=10) #(파일이름,파일 하나의 사이즈, 총 파일 갯수)
    file_handler.setLevel(logging.WARNING)  # 어느 단계까지 로깅을 할지를 적어줌
    app.logger.addHandler(file_handler) # app.logger.addHandler() 에 등록시켜줘야! app.logger 로 사용 가능


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('이것은 중요한 에러입니다. page_not_found에서 일어났습니다.') #404에러시 ()안에 있는 로그를 남겨라 #flask_logging_basic.py참고
    #즉 에러가 발생하면 app.logger에 위의 로그를 남기는 것
    return "<h1>해당 경로에 맞는 웹페이지가 없습니다. 문제가 지속되면 관리자에게 연락해주세요</h1>", 404
    #return은 해당 에러가 났을 때, 사용자에게 보여지는 페이지


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=False)

    
    #다음과 같이 debug 옵션을 써줄 경우, app.debug 에 해당 값이 들어가고, debug=True 일 경우, 상세 정보를 화면에 표시
    #주로 개발/테스트시 사용
    #상용화시에는 app.debug 를 False 로 놓고, 디버그 정보를 로그로 남기는 것이 일반적임(왜냐면 true로 해놓으면 모든 debug 정보들이 어차피 나오므로)
    #즉 위에서 debug 옵션이 true이면 로그는 발생하지 않음
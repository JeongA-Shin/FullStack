'''
### 6.2. 로깅(logging) 다루기
- 서버는 24시간 동작하므로 문제가 있을 때 어떤 문제가 있었는지 파악하기 위해 로깅 기능을 사용함
- 상용화시 다양한 문제(해킹, 사용자 모니터링등)에 대해서도 로깅 기능을 활용할 수 있음

### 간단한 logging 라이브러리 사용법

- 파이썬에는 로그를 다루는 logging 라이브러리가 있음
- 로딩 정보는 레벨이 있음
- 로깅 정보는 로그의 레벨에 따라서 출력을 제한 할 수 있음
  - DEBUG > INFO > WARNING > ERROR > Critical
'''



import logging #파이썬 자체에 logging이라는 라이브러리가 있고, flask 안에 logging이라는 라이브러리도 있음
# 파일로 남기기 위해서는 filename='test.log' 파라미터, 어느 레벨의 로그까지 남길 것인지를 level 로 설정 가능
#만약 DEBUG로 한다면 모든 로그를 남긴다는 의미
logging.basicConfig(filename='test.log', level=logging.ERROR)

# 로그를 남길 부분에 다음과 같이 로그 레벨에 맞추어 출력해주면 해당 내용(()안의 문자열)이 파일에 들어감(flask_logging.py 참고)
logging.debug("debug 발생")
logging.info("info 발생")
logging.warning("warning 발생")
logging.error("error 발생")
logging.critical("critical 발생")
from flask import Flask,jsonify,request
#request는 url에 여러 파라미터 값들을 붙이기 위해 import함
#https://post.naver.com/viewer/postView.naver?volumeNo=32113292&memberNo=49649230&searchRank=51
#위의 url에서 volumeNo,memeberNo,searchRank 등이 url의 파라미터임
#당연히 각 파라미터(키)의 값은 32113292,49649230,51이 됨

app=Flask(__name__) #객체


@app.route('/login')
def login():
    username=request.args.get('user_name')#http방식으로 주고받는 데이터(url의 파라미터로 표현됨) 중 user_name의 value를 username 변수에 담음
    passwd = request.args.get('pw')
    email = request.args.get('email_address')
    print (username, passwd, email)

    if username=='dave': #url의 파라미터들의 해당 key의 값이 dave이면
        return_data={'auth':'success'}
    else:
        return_data={'auth':'failed'}
    return jsonify(return_data)



if __name__=='__main__':
    app.run(host='192.168.123.195',port="8080",debug=True)

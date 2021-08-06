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

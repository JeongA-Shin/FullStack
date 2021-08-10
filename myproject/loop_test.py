from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello_loop')
def hello_name():
    value_list = ['list1', 'list2', 'list3']
    return render_template('loop.html', values=value_list) #loop.html을 부르되, html의 values는 value_list를 전달

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
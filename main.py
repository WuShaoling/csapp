from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello,World!'


# 只在测试的时候运行
if __name__ == '__main__':
    app.run("127.0.0.1", 5000)

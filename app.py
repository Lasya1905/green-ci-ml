from flask import Flask
import math
import time
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Energy-Aware CI/CD Project!"

@app.route("/compute")
def compute():
    data = [i*i for i in range(500_000)]
    return str(sum(data))

@app.route('/memory')
def memory():
    data = [i for i in range(1_000_000)]
    return str(len(data))


if __name__ == '__main__':
    app.run()

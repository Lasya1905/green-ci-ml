from flask import Flask
import math
import time
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Energy-Aware CI/CD Project!"

@app.route("/compute")
def compute():
    total = 0
    for i in range(700_000):
        if i % 3 == 0:
            total += i
        elif i % 3 == 1:
            total -= i
        else:
            total += i // 2
    return str(total)

@app.route('/memory')
def memory():
    data = [i for i in range(1_000_000)]
    return str(len(data))


if __name__ == '__main__':
    app.run()

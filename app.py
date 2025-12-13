from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Energy-Aware CI/CD Project!"

@app.route('/compute')
def compute():
    s = 0
    for i in range(1500):
        for j in range(1500):
            s += i * j
    return str(s)

@app.route('/memory')
def memory():
    data = [i for i in range(1_000_000)]
    return str(len(data))


if __name__ == '__main__':
    app.run()

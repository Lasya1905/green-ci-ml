from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Energy-Aware CI/CD Project!"

@app.route('/compute')
def compute():
    x = 0
    for i in range(500000):
        x += i
    return str(x)


if __name__ == '__main__':
    app.run()

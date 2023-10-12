from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, DOCKER is Working from inside AWS EC2 or AWS APP RUNNER!</p>"


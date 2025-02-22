from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "Hi from flask app!!!"})


@app.route('/actuator/healthz')
def health():
    return jsonify({"status": "UP"})


@app.route('/user')
def user():
    return jsonify({"user": "tao"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

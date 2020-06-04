from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return 'This a GET method'
    if request.method == 'POST':
        return 'This a POST method'


@app.route('/json')
def json():
    return jsonify({"key1": "value1", "key2": "value2"})


@app.route('/body', methods=['POST'])
def post():
    body = request.json
    return "Hi I'm {}, I'm {} years old".format(body["name"], body["age"])


if __name__ == "__main__":
    app.run(port="5000", debug=True)

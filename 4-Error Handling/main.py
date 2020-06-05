from flask import Flask, abort
import werkzeug

app = Flask(__name__)


@app.route('/test1', methods=['POST'])
def example_405():
    # Only a POST request is allowed
    return 'This is a POST'


@app.route('/test2')
def example_():
    return "I'm a teapot", 418


@app.route('/test3')
def post():
    abort(418)


# How to register a custom error handler?
@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400


def handle_not_found(e):
    return "Sorry, I haven't found that", 404


app.register_error_handler(404, handle_not_found)

if __name__ == "__main__":
    app.run(port="5000", debug=True)

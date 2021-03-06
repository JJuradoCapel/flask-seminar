from flask import Flask, render_template
import werkzeug

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run(port="5000", debug=True)

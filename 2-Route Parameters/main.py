from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index'


@app.route('/users/<name>')
def username(name):
    return 'Your name is {}'.format(name)


@app.route('/sum/<int:num>')
def sum_value(num):
    return '5 plus your number is {}'.format(5 + num)


@app.route('/total/<int:num1>/<int:num2>/<int:num3>')
def total_sum(**params):
    return 'The total sum is {}'.format(sum(params.values()))


if __name__ == "__main__":
    app.run(port="5000", debug=True)

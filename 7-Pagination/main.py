from db import get_users
from flask import Flask, render_template, request, abort, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST'])
def paginated_users():
    users = get_users()
    # Add the logic to handle a pagination with start, end and step query parameters
    query_params = request.args

    return []

# EXTRA: Create the pagination as a decorator

if __name__ == "__main__":
    app.run(port="5000", debug=True)

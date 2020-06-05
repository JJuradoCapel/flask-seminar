import werkzeug
import json

from db import db
from flask import Flask, render_template, request, abort, jsonify
from models import create_user_model
from bson.json_util import dumps
from utils import get_user

app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return dumps(list(db.users.find()))
    if request.method == 'POST':
        errors = create_user_model.validate(request.json)
        if errors:
            abort(400, description=str(errors))
        new_user = request.json

        result = db.users.find_one({"username": new_user["username"]})
        if result != None: return abort(400, "User already exist") 

        db.users.insert_one(new_user)
        return {}, 201


@app.route('/users/<username>')
@get_user
def get_user_info(user):
    return dumps(user)


def handle_bad_request(e):
    return jsonify(error=str(e)), 400
app.register_error_handler(400, handle_bad_request)

if __name__ == "__main__":
    app.run(port="5000", debug=True)

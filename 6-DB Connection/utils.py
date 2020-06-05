import functools
from flask import abort
from db import db

def get_user(func):
    @functools.wraps(func)
    def wrapper(username):
        result = db.users.find_one({"username": username})
        if result == None: abort(404, "User nor found")
        return func(result)
    return wrapper


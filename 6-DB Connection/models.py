from marshmallow import Schema, fields

class CreateUser(Schema):
    name = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)

create_user_model = CreateUser()

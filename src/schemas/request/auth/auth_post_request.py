from marshmallow import Schema, fields, validate


class AuthPostRequest(Schema):
    email = fields.Email(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)

from marshmallow import Schema, fields


class AuthPostRequest(Schema):
    email = fields.Email(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)

from marshmallow import Schema, fields, validate


class UserPostRequest(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    phone_number = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(
        required=True,
        validate=[
            validate.Length(min=6, max=30, error="The password length must be [6-30]."),
            validate.Regexp(regex=r'[A-Z]', error="The password must contain at least one uppercase letter.")
        ]
    )

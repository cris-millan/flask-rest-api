from marshmallow import Schema, fields, validate


class UserQuerySchema(Schema):
    id = fields.UUID(required=True, allow_none=False)

class UserSchema(Schema):
    first_name = fields.Str(required=False, allow_none=True)
    last_name = fields.Str(required=False, allow_none=True)
    phone_number = fields.Str(required=False)
    # password = fields.Str(
    #     required=False,
    #     load_only=True,
    #     allow_none=False,
    #     validate=[
    #         validate.Length(min=8, max=8, error="La contraseña debe tener exactamente 8 caracteres."),
    #         validate.Regexp(regex=r'[A-Z]', error="La contraseña debe contener al menos una letra mayúscula.")
    #     ],
    # )

class UserPatchRequest(Schema):
    user = fields.Nested(UserSchema, required=True)
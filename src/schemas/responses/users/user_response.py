from marshmallow import Schema, fields


class UserResponse(Schema):
    id = fields.UUID(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone_number = fields.Str(required=True)
    created_at = fields.DateTime()

    class Meta:
        # Define el orden deseado de las claves
        ordered = True

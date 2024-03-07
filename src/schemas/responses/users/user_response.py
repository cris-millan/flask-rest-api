from marshmallow import Schema, fields


class UserResponse(Schema):
    id = fields.UUID(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone_number = fields.Str(required=True)
    is_log_in = fields.Boolean(required=True)
    is_email_verify = fields.Boolean(required=True)
    is_phone_verify = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True)
    modified_at = fields.DateTime(required=True)
    created_by_id = fields.UUID(dump_only=True)
    modified_by_id = fields.UUID(dump_only=True)
    role_id = fields.UUID(dump_only=True)

    class Meta:
        # Define el orden deseado de las claves
        ordered = True

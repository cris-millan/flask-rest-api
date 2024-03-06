from marshmallow import Schema, fields, validate, ValidationError


class UserGetRequestSchema(Schema):
    id = fields.UUID(required=False, allow_none=False)
    email = fields.Str(required=False, allow_none=False)
    name = fields.Str(required=False, allow_none=False)
    phone_number = fields.Str(required=False, allow_none=False)
    status = fields.Str(required=False, allow_none=True, validate=validate.OneOf(["active", "inactive"]))


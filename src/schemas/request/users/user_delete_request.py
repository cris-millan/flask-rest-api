from marshmallow import Schema, fields, validate


class UserDeleteRequest(Schema):
    id = fields.UUID(required=False, allow_none=False)

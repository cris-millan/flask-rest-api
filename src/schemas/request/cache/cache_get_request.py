from marshmallow import Schema, fields


class CacheGetRequest(Schema):
    key = fields.Str(required=True, allow_none=False)

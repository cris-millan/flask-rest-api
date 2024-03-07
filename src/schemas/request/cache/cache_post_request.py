from marshmallow import Schema, fields


class CachePostRequest(Schema):
    key = fields.Str(required=True, allow_none=False)
    value_str = fields.Str(required=False, allow_none=False)
    value_dict = fields.Dict(required=False, allow_none=False)

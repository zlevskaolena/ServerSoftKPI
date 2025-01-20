from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))

class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    amount = fields.Float(required=True)
    timestamp = fields.Str(dump_only=True)

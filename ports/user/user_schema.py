from marshmallow import Schema, fields, pre_load, post_dump

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    password = fields.Str(load_only=True)
    gender = fields.Int()
    sign = fields.Str()
    intro = fields.Str()
    address = fields.Str()
    birthday = fields.Str()
    token = fields.Str()

    @pre_load
    def make_user_data(self, data):
        return data

    @post_dump
    def dump_user(self, data):
        return {'user': data}

    class Meta:
        strict = True


user_schema = UserSchema()
user_schemas = UserSchema(many=True)
from marshmallow import Schema, fields, pre_load, post_dump

class UserSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    subtitle = fields.Str()
    intro = fields.Str()
    logo = fields.Str()

    @pre_load
    def make_user_data(self, data):
        return data

    @post_dump
    def dump_user(self, data):
        return data

    class Meta:
        strict = True


blog_schema = UserSchema()
blog_schemas = UserSchema(many=True, strict=True)
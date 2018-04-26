from wtforms.validators import ValidationError
from ports.user.model.user import User

class EmailExsits(object):

    def __init__(self, message='电子邮件重复'):
        self.message = message

    def __call__(self, form, field):
        email = field.data
        count = User.query.filter_by(email=email).count()
        if count > 0:
            raise ValidationError(self.message)

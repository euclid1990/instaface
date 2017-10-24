from wtforms.validators import ValidationError

class Unique(object):
    def __init__(self, model, field, message="This element already exists."):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field==field.data).first()
        if check:
            raise ValidationError(self.message)


class CurrentPassword(object):
    def __init__(self, model, message="The password you entered does not match your current password."):
        self.model = model
        self.message = message

    def __call__(self, form, field):
        user_id = form.user_id
        user = self.model.query.filter_by(id=user_id).first()
        if user is None or user.check_password(field.data) is False:
            raise ValidationError(self.message)

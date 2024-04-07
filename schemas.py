from marshmallow import fields, Schema, validate, ValidationError
import re


def validate_password(password):
    if not password:
        raise ValidationError('Password is required')
    if not re.match(r'\d.*[A-Z]|[A-Z].*\d', password):
        raise ValidationError(
            'Password must contain 1 capital letter and 1 number')


class UserSchema(Schema):
    id = fields.String(dump_only=True)
    username = fields.String(
        required=True, validate=validate.Length(min=4, max=20))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=[
                             validate.Length(min=5, max=50), validate_password])

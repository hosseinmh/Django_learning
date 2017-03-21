from django.core.exceptions import ValidationError

def auther_email(value):
    if not "@" in value:
        raise ValidationError("Not a valid email")
    return value



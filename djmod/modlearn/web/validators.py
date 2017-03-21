from django.core.exceptions import ValidationError

def auther_email(value):
    if "@" in value:
        return value
    else:
        raise ValidationError("Not a valid email")

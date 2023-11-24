import re

from django.core.exceptions import ValidationError


def custom_validator_alphanumundersc(value):
    pattern = r'[a-zA-Z0-9_]+'
    if re.fullmatch(pattern, value) is None :
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

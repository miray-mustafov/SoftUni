from django.core.exceptions import ValidationError

REQUIRED_LENGTH = 2
MIN_YEAR = 1980
MAX_YEAR = 2049


def validate_min_len(value):
    if len(value) < REQUIRED_LENGTH:
        raise ValidationError('The username must be a minimum of 2 chars')


def validate_year(value):
    if not MIN_YEAR <= value <= MAX_YEAR:
        raise ValidationError('Year must be between 1980 and 2049')

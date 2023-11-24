from enum import Enum

from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from petstagram.core.model_mixins import ChoicesEnumMixin


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do no show'


class PetstagramUser(AbstractUser):
    MIN_LEN_FL_NAME = 2
    MAX_LEN_FL_NAME = 30

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=MAX_LEN_FL_NAME, validators=[MinLengthValidator(MIN_LEN_FL_NAME)])
    last_name = models.CharField(max_length=MAX_LEN_FL_NAME, validators=[MinLengthValidator(MIN_LEN_FL_NAME)])
    profile_picture = models.URLField(blank=True)
    gender = models.CharField(max_length=Gender.max_len(), choices=Gender.choices())

    # wizardawizarda
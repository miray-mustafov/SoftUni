from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from mid_exam.web.validators import validate_min_len, validate_year


class Profile(models.Model):
    REQUIRED_AGE = 18

    username = models.CharField(blank=False, null=False, max_length=10, validators=[validate_min_len, ], )
    email = models.EmailField(blank=False, null=False, )
    age = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(REQUIRED_AGE), ], )
    password = models.CharField(blank=False, null=False, max_length=30, )

    first_name = models.CharField(blank=True, null=True, max_length=30, )
    last_name = models.CharField(blank=True, null=True, max_length=30, )
    profile_picture = models.URLField(blank=True, null=True, )

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f'{self.username}'


class Car(models.Model):
    CAR_TYPE_CHOICES = [
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    ]
    type = models.CharField(blank=False, null=False, max_length=10, choices=CAR_TYPE_CHOICES, )
    model = models.CharField(blank=False, null=False, max_length=20, validators=[MinLengthValidator(2)], )
    year = models.IntegerField(blank=False, null=False, validators=[validate_year, ], )
    image_url = models.URLField(blank=False, null=False, )
    price = models.FloatField(blank=False, null=False, validators=[MinValueValidator(1.0), ], )

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f'{self.model} {self.type} id:{self.pk}'

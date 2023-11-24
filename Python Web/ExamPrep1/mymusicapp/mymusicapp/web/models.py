from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models
from mymusicapp.web.validators import custom_validator_alphanumundersc


class Profile(models.Model):
    n = models.CharField(null=False, blank=True, max_length=30)
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2), custom_validator_alphanumundersc, ],
        unique=True,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    age = models.PositiveIntegerField(
        validators=[MaxValueValidator(200)],
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'id: {self.pk} uname: {self.username}'


class Album(models.Model):
    GENRE_CHOICES = [
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    ]
    name = models.CharField(unique=True, max_length=30, blank=False, null=False, )
    artist = models.CharField(max_length=30, blank=False, null=False, )
    genre = models.CharField(max_length=30, blank=False, null=False, choices=GENRE_CHOICES)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=254, blank=False, null=False)
    price = models.FloatField(blank=False, null=False, validators=[MinValueValidator(0.0), ], )

    def __str__(self):
        return f'{self.name} by {self.artist}'

    class Meta:
        ordering = ('pk',)

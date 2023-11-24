from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.template.defaultfilters import slugify

UserModel = get_user_model()


# PETS / MODElS
class Pet(models.Model):
    MAX_NAME = 30
    MIN_NAME = 2

    name = models.CharField(max_length=MAX_NAME, validators=[MinLengthValidator(MIN_NAME)], )
    photoo = models.URLField(max_length=254)
    date_of_birth = models.DateField(blank=True, null=True, )
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        default=1,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:  # change on update or not
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Pet: {self.name} id:{self.pk}"

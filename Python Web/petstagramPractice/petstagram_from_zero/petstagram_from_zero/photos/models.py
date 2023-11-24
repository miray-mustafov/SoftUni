from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator

from petstagram_from_zero.pets.models import Pet
from petstagram_from_zero.photos.validators import validate_file_size

UserModel = get_user_model()


# PHOTO / MODELS
class Photo(models.Model):
    photo = models.ImageField(upload_to='pet_photos', null=False, validators=[validate_file_size])
    description = models.TextField(max_length=300, validators=[MinLengthValidator(10)], blank=True, null=True, )
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True, )  # TODO check null
    date_of_publication = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        default=1
    )

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f"Photo: {self.photo.name.split('/')[-1]} ({self.pk})"

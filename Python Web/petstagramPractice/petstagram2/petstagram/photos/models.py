from django.db import models
from django.core.validators import MinLengthValidator
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size


class Photo(models.Model):
    photo = models.ImageField(upload_to='pet-photos', null=False, validators=(validate_file_size,))
    description = models.TextField(max_length=300, validators=(MinLengthValidator(10),), blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True,)
    date_of_publication = models.DateField(auto_now=True)

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f"Photo: {self.photo.name.split('/')[-1]} ({self.pk})"

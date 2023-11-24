from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False,)
    date_of_birth = models.DateField(blank=True, null=True,)
    personal_photo = models.URLField(null=False, blank=False, max_length=250,)
    slug = models.SlugField(unique=True, null=False, blank=True,)  # name-id

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:  # change on update or not
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} {self.name}'
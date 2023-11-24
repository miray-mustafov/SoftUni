from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    text = models.TextField(max_length=300, null=False, blank=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date_time_of_publication"]


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

from django.contrib.auth import get_user_model
from django.db import models

from petstagram_from_zero.photos.models import Photo

UserModel = get_user_model()


class Comment(models.Model):
    text = models.TextField()
    date_of_publication = models.DateField(auto_now=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        # default=1, DONE in 0002 migration
    )

    class Meta:
        ordering = ["-date_of_publication"]

    def __str__(self):
        return f'Comment: {self.pk} txt: {self.text} to_photo: {self.to_photo}'


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        default=1,
    )

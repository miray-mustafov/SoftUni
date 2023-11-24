from django import forms

from petstagram.photos.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('date_of_publication',)
        labels = {
            'photo': 'Photo file',
            'tagged_pets': 'Tag Pets',
        }
        # widgets = {
        #     'description': forms.TextInput(attrs={'placeholder': 'desc'})
        # }


class PhotoCreateForm(PhotoForm):
    pass


class PhotoEditForm(PhotoForm):
    class Meta:
        model = Photo
        exclude = ('photo',)
        labels = {
            'tagged_pets': 'Tag Pets',
        }


class PhotoDeleteForm(PhotoForm):
    pass

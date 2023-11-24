from django import forms

from petstagram_from_zero.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        labels = {
            'photo': 'Photo file',
            'tagged_pets': 'Tag Pets',
        }


class PhotoAddForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('user',)
        labels = {
            'photo': 'Photo file',
            'tagged_pets': 'Tag Pets',
        }


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('photo', 'user')

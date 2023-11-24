from petstagram.pets.models import Pet
from django import forms


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('slug',)
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Link to Image',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Pet Name"}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'placeholder': "dd/mm/yyyy"}),
            'personal_photo': forms.TextInput(attrs={'placeholder': "Link to Image"}),
        }


class PetCreateForm(PetForm):
    pass


class PetEditForm(PetForm):
    pass


class PetDeleteForm(PetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True

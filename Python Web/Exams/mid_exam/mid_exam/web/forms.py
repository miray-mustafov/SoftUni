from django import forms

from mid_exam.web.models import Profile, Car


# TOD password = forms.CharField(widget=forms.PasswordInput)
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password', ]
        widgets = {'password': forms.PasswordInput()}


class ProfileEditForm(ProfileForm):
    pass


class ProfileDeleteForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):  #
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'image_url': "Image URL"
        }


class CarCreateForm(CarForm):
    pass


class CarEditForm(CarForm):
    pass


class CarDeleteForm(CarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

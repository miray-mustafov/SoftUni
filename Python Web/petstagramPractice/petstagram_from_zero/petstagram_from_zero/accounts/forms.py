from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserRegisterForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email")
        # field_classes = {"username": auth_forms.UsernameField}


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('personal_photo', 'first_name', 'last_name', 'email', 'gender',)
        labels = {
            'personal_photo': 'Image',
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last_name',
            'email': 'Email',
            'gender': 'Gender',
        }

# class UserLoginForm(auth_forms.AuthenticationForm):
#     pass

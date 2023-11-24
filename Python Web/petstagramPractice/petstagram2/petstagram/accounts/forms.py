from django.contrib.auth import get_user_model, forms as auth_forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms

UserModel = get_user_model()


class PetstagramUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email',)
        field_classes = {
            'username': auth_forms.UsernameField,
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'placeholder': 'Username'}),
    )


class PetstagramUserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name',)
        field_classes = {'username': auth_forms.UsernameField}


# class PetstagramUserEditForm(forms.ModelForm):
#     class Meta():
#         model = UserModel
#         fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender',)
#         exclude = ('password', )
#         labels = {
#             'username': 'Username',
#             'first_name': 'First Name',
#             'last_name': 'Last Name',
#             'email': 'E-mail',
#             'profile_picture': 'Image',
#             'gender': 'Gender',
#         }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Password'}),
    )

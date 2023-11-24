from .models import Employee
from django import forms
class EmployeeForm(forms.Form):
    your_name = forms.CharField(label='Your name:', max_length=30)
    url_field = forms.URLField(initial='http://',)

    CHOICES = (
        ('1', 'Option One'),
        ('2', 'Option Two'),
        ('3', 'Option Three'),
    )
    choice_field = forms.ChoiceField(choices=CHOICES)
    char_field = forms.CharField(widget=forms.RadioSelect(choices=CHOICES[:2]))
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols': 80, 'rows': 10,
                   'class': 'special',
                   'title': 'Add a comment'}))

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
from petstagram_from_zero.common.models import Comment
from django import forms


class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add comment...'})
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search by pet name...'}))

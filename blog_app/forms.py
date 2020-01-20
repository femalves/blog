from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25, widget=forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'Email', 'type': 'email'}))
    to = forms.EmailField(widget=forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'Email to', 'type': 'email'}))
    comments = forms.CharField(required=False,
                               widget=forms.Textarea(attrs={'class': 'uk-textarea', 'placeholder': 'Comment'}))


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'Email', 'type': 'email'}),
            'body': forms.Textarea(attrs={'class': 'uk-textarea', 'placeholder': 'Comment'}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'class': 'search'}))

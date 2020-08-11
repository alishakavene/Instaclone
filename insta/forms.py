from django import forms
from .models import Post


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

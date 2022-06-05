from django import forms
from .models import Post

class mallikaavio(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title','author', 'body')

    widgets = {
      'title':forms.TextInput(attrs= {'class': 'form-control','placeholder':'Otsikko'}),
      'author':forms.Select(attrs= {'class': 'form-control','placeholder':'Otsikko'}),
      'body':forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'Blogi teksti'})
    }
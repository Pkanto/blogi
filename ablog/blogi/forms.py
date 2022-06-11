from django import forms
from .models import Post, Kategoria

lista = Kategoria.objects.all().values_list('nimi','nimi')

choise = []

for i in lista:
  choise.append(i)


class mallikaavio(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title','author','kategoria', 'body')

    widgets = {
      'title':forms.TextInput(attrs= {'class': 'form-control','placeholder':'Otsikko'}),
      'author':forms.TextInput(attrs= {'class': 'form-control','value':'','id':'id','type':'hidden'}),
      #'author':forms.Select(attrs= {'class': 'form-control'}),
      'kategoria':forms.Select(choices= choise, attrs= {'class': 'form-control'}),
      'body':forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'Blogi teksti'})
    }
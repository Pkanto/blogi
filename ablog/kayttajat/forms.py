from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blogi.models import Profiili
from django.db import models

#tyylitelty käyttäjä rekisteröityminen sivusto

class Kirjaudu(UserCreationForm):
  email = forms.EmailField(widget= forms.EmailInput(attrs= {'class': 'form-control'}))
  first_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs= {'class': 'form-control'}))
  last_name = forms.CharField(max_length = 100,widget = forms.TextInput(attrs= {'class': 'form-control'}))

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
  
  def __init__(self, *args, **kwargs):
    super(Kirjaudu, self).__init__( *args, **kwargs)  
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'


#Lomake jolla muokataan käyttäjä profiilia ja sen tyyöittely
class MuokkaaProfiialomake(UserChangeForm):
  email = forms.EmailField(widget= forms.EmailInput(attrs= {'class': 'form-control'}))
  first_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs= {'class': 'form-control'}))
  last_name = forms.CharField(max_length = 100,widget = forms.TextInput(attrs= {'class': 'form-control'}))
  username = forms.CharField(max_length = 100,widget = forms.TextInput(attrs= {'class': 'form-control'}))
  last_login = forms.CharField(max_length = 100,widget = forms.TextInput(attrs= {'class': 'form-control'}))
  is_superuser = forms.CharField(max_length = 100,widget = forms.CheckboxInput(attrs= {'class': 'form-check'}))
  is_staff = forms.CharField(max_length = 100,widget = forms.CheckboxInput(attrs= {'class': 'form-check'}))
  is_active = forms.CharField(max_length = 100,widget = forms.CheckboxInput(attrs= {'class': 'form-check'}))
  date_joined = forms.CharField(max_length = 100,widget = forms.TextInput(attrs= {'class': 'form-control'}))

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active','date_joined')
  
  #Lomake jolla salasana vaihdetaan tyylittelyä

class SalasanaVaihtolomake(PasswordChangeForm):
  old_password = forms.CharField(widget= forms.PasswordInput(attrs= {'class': 'form-control', 'type':'password'}))
  new_password1 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs= {'class': 'form-control', 'type':'password'}))
  new_password2 = forms.CharField(max_length = 100,widget = forms.PasswordInput(attrs= {'class': 'form-control', 'type':'password'}))

  class Meta:
    model = User
    fields = ('old_password', 'new_password1', 'new_password2')

class ProfiiliSivuLuonti(forms.ModelForm):
  class Meta:
    model = Profiili
    fields =('bio', 'profiili_kuva','some_fb','some_insta','some_linke')
    widgets = {
        'bio':forms.Textarea(attrs= {'class': 'form-control','placeholder':'Otsikko'}),
        #'profiili_kuva':forms.TextInput(attrs= {'class': 'form-control','value':'','id':'id','type':'hidden'}),
        'some_fb':forms.TextInput(attrs= {'class': 'form-control'}),
        'some_insta':forms.TextInput(attrs= {'class': 'form-control'}),
        'some_linke':forms.TextInput(attrs= {'class': 'form-control'}),
      }
    
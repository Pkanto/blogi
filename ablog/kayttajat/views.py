from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import Kirjaudu

class TeeKayttaja(generic.CreateView):
    form_class = Kirjaudu
    template_name = 'registration/rekisteroi.html'
    success_url = reverse_lazy('login')

from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import Kirjaudu, MuokkaaProfiialomake,SalasanaVaihtolomake

class Salasanavaihto(PasswordChangeView):
    form_class = SalasanaVaihtolomake
    success_url = reverse_lazy('salasana_vaihto')

class TeeKayttaja(generic.CreateView):
    form_class = Kirjaudu
    template_name = 'registration/rekisteroi.html'
    success_url = reverse_lazy('login')

class MuokkaaKayttajaa(generic.UpdateView):
    form_class = MuokkaaProfiialomake
    template_name = 'registration/muokkaa_profiilia.html'
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user

def salasana_onnistui(request):
    return render(request, 'registration/salasana_onnistui.html', {})
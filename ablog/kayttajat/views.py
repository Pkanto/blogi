from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import Kirjaudu, MuokkaaProfiialomake,SalasanaVaihtolomake
from blogi.models import Profiili


class NaytaProfiili(DetailView):
    model = Profiili
    template_name = 'registration/kayttaja_profiili.html'

    def get_context_data(self, *args, **kwargs): #hakee kirjautuneen käyttäjän ID ja antaa sen käyttöön
        kayttaja = get_object_or_404(Profiili, id = self.kwargs['pk'])
        context = super(NaytaProfiili, self).get_context_data(*args, **kwargs)
        context["kayttaja"] = kayttaja
        return context

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
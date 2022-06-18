from django.contrib import admin
from django.urls import path, include
from .views import TeeKayttaja,MuokkaaKayttajaa, Salasanavaihto,NaytaProfiili
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('rekistroi/', TeeKayttaja.as_view(), name='rekisteroi'),
    path('muokkaa/', MuokkaaKayttajaa.as_view(), name='muokkaa'),
    path('password/',Salasanavaihto.as_view(template_name='registration/vaihda_salasana.html')),
    path('salasana_onnistui', views.salasana_onnistui, name='salasana_vaihto'),
    path('<int:pk>/kayttajaprofiili',NaytaProfiili.as_view(), name = 'nayta_profiili'),
]

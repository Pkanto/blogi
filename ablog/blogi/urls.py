from django.contrib import admin
from django.urls import path, include
from . import views
from .views import HomeView, Artikkeli, kirjoitaBlogi, Paivita, Poista, TeeKategoria, Kategoriat, LikeView, kirjoitaKommentti


urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('artikkeli/<int:pk>', Artikkeli.as_view(), name = 'artikkeli'),
    path('blogin/', kirjoitaBlogi.as_view(), name= 'bloggin'),
    path('lisaa_kategoria/', TeeKategoria.as_view(), name= 'kategoria'),
    path('artikkeli/paivita/<int:pk>', Paivita.as_view(), name = 'paivita'),
    path('artikkeli/<int:pk>/poista', Poista.as_view(), name = 'poista'),
    path('kategoria/<str:kat>/', Kategoriat, name = 'kategori'),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    path('artikkeli/<int:pk>/kommentti/',kirjoitaKommentti.as_view(),name='kommentti_kirjoitus'),
]

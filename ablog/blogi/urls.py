from django.contrib import admin
from django.urls import path, include
from . import views
from .views import HomeView, Artikkeli, kirjoitaBlogi


urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('artikkeli/<int:pk>', Artikkeli.as_view(), name = 'artikkeli'),
    path('blogin/', kirjoitaBlogi.as_view(), name= 'bloggin'),
]

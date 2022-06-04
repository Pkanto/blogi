from django.contrib import admin
from django.urls import path, include
from . import views
from .views import HomeView, Artikkeli


urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('artikkeli/<int:pk>', Artikkeli.as_view(), name = 'artikkeli'),
]

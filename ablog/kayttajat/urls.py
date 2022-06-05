from django.contrib import admin
from django.urls import path, include
from .views import TeeKayttaja



urlpatterns = [
    path('rekistroi/', TeeKayttaja.as_view(), name='rekisteroi'),
]

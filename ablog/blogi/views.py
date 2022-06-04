from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# Create your views here.
#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
  model = Post
  template_name = 'home.html'
class Artikkeli(DetailView):
  model = Post
  template_name = 'artikkeli.html'
class kirjoitaBlogi(CreateView):
  model = Post
  template_name = 'blogging.html'
  fields = '__all__'
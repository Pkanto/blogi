from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import mallikaavio
from django.urls import reverse_lazy


# Create your views here.
#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  ordering = ['-julkaisu']

class Artikkeli(DetailView):
  model = Post
  template_name = 'artikkeli.html'

class kirjoitaBlogi(CreateView):
  model = Post
  form_class = mallikaavio
  template_name = 'blogging.html'
  success_url = reverse_lazy('home')
  #fields = ('title', 'body')

class Paivita(UpdateView):
  model = Post
  template_name = 'Editoi.html'
  fields = ['title', 'body']

class Poista(DeleteView):
  model = Post
  template_name = 'poista.html'
  success_url = reverse_lazy('home')
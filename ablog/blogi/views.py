from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Kategoria
from .forms import mallikaavio
from django.urls import reverse_lazy


# Create your views here.
#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  kats = Kategoria.objects.all()
  ordering = ['-julkaisu']

  def get_context_data(self, *args, **kwargs):
    kat_lista = Kategoria.objects.all()
    context = super(HomeView, self).get_context_data(*args, **kwargs)
    context["kat_lista"] = kat_lista
    return context

def Kategoriat(request, kat):
  kategoria_posts = Post.objects.filter(kategoria = kat.capitalize().replace('-',' '))
  return render(request, 'kategoriat.html',{'kat':kat.replace('-',' ').capitalize(), 'kategoria_posts':kategoria_posts})


class Artikkeli(DetailView):
  model = Post
  template_name = 'artikkeli.html'

class kirjoitaBlogi(CreateView):
  model = Post
  form_class = mallikaavio
  template_name = 'blogging.html'
  success_url = reverse_lazy('home')
  

class TeeKategoria(CreateView):
  model = Kategoria
  fields ='__all__'
  template_name = 'kategoria.html'
  success_url = reverse_lazy('home')

class Paivita(UpdateView):
  model = Post
  template_name = 'Editoi.html'
  fields = ['title', 'body']

class Poista(DeleteView):
  model = Post
  template_name = 'poista.html'
  success_url = reverse_lazy('home')


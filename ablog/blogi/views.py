from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Kategoria,Kommentoi
from .forms import mallikaavio, malliKommentoi
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# Create your views here.
#def home(request):
#   return render(request, 'home.html', {})

#Tee alkusivulle View pohja käyttämään lista näkymää Post näkymä
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

#Artikkeli sivulle näkymä pohja käyttämään Post mallia
class Artikkeli(DetailView):
  model = Post
  template_name = 'artikkeli.html'

  #lisää artikkelit tiputus valikko myös artikkelit sivulle ja tykkäykset 
  def get_context_data(self, *args, **kwargs):
    kat_lista = Kategoria.objects.all()
    context = super(Artikkeli, self).get_context_data(*args, **kwargs)

    random  = get_object_or_404(Post, id = self.kwargs['pk'])
    tykkaykset_yhteensa = random.tykkaykset_yhteensa()
    
    liked = False
    if random.likes.filter(id = self.request.user.id).exists():
      liked = True
    context["kat_lista"] = kat_lista
    context["tykkaykset_yhteensa"] = tykkaykset_yhteensa
    context["liked"] =liked
    return context


#Blogin kirjoitus sivu käyttämään Post mallia 
class kirjoitaBlogi(CreateView):
  model = Post
  form_class = mallikaavio
  template_name = 'blogging.html'
  success_url = reverse_lazy('home')
  
#Kategorioiden teko sivulle näkymä 
class TeeKategoria(CreateView):
  model = Kategoria
  fields ='__all__'
  template_name = 'kategoria.html'
  success_url = reverse_lazy('home')


#Blogi sivujen päivitys nkymä
class Paivita(UpdateView):
  model = Post
  template_name = 'Editoi.html'
  fields = ['title', 'body']


#Blogin poisto sivujen näkymä teko
class Poista(DeleteView):
  model = Post
  template_name = 'poista.html'
  success_url = reverse_lazy('home')

def LikeView(request,pk):
  post = get_object_or_404(Post, id=request.POST.get('post_id'))
  liked = False
  if post.likes.filter(id=request.user.id).exists():
    post.likes.remove(request.user)
    liked = False
  else:
    post.likes.add(request.user)
    liked = True
  return HttpResponseRedirect(reverse('artikkeli', args=[str(post.pk)]))

#Kommettien kirjoitus näkymä
class kirjoitaKommentti(CreateView):
  model = Kommentoi
  form_class = malliKommentoi
  template_name = 'Lisaa_kommentti.html'
  success_url = reverse_lazy('home')
  #Lisää käyttäjän blogi kommentteihin
  def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

  



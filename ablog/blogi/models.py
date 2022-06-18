from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Kategoria(models.Model):
  nimi = models.CharField(max_length = 255)

  def __str__(self):
    return self.nimi 

  def get_absolute_url(self):
    return reverse('home')

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length = 255)
  author = models.ForeignKey(User, on_delete= models.CASCADE)
  kategoria = models.CharField(max_length = 255, default = 'ei kategoriaa')
  body = RichTextField(blank = True, null = True) 
  kuvan_malli = models.ImageField(null=True, blank=True, upload_to ='images/')#kuvan lisäys malli blogin teko sivulle
  julkaisu = models.DateField(auto_now_add= True)
  likes = models.ManyToManyField(User, related_name='blogi_posts')

  #tykkäysten määrä 
  def tykkaykset_yhteensa(self):
    return self.likes.count()
  
  def __str__(self):
    return self.title + ' | ' + str(self.author)

  def get_absolute_url(self):
    return reverse('home')

class Profiili(models.Model):
  user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
  bio = models.TextField()
  profiili_kuva = models.ImageField(null = True, blank = True,upload_to ='images/profiili/') #proffilin mallin editointi salliin oneToone liitoksen tietokantaan
  some_fb = models.CharField(max_length = 255, null = True, blank = True)
  some_insta = models.CharField(max_length = 255, null = True, blank = True)
  some_linke = models.CharField(max_length = 255, null = True, blank = True)
  

  def __str__(self):
    return str(self.user)
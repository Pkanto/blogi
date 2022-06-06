from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


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
  body = models.TextField()
  julkaisu = models.DateField(auto_now_add= True)
  

  def __str__(self):
    return self.title + ' | ' + str(self.author)

  def get_absolute_url(self):
    return reverse('home')
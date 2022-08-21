from django.db import models
from django.contrib.auth.models import User
from operator import truediv
from statistics import mode
from django.db import models


class Publisher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="avatars", null=True, blank=True)
    


class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="avatars", null=True, blank=True)

    def __str__(self):
        return self.titulo

from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nombreCompleto = models.CharField(max_length=150)
    area = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    segmento = models.SmallIntegerField()
    perfil = models.CharField(max_length=50)
    
    def get_full_name(self):
        return f'{self.first_name}{self.last_name}'


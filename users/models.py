from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    
    def get_full_name(self):
        return f'{self.first_name}{self.last_name}'


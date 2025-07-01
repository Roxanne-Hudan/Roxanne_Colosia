from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"Avatar de {self.user.username}"


class Profesor(models.Model): 
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=100) 
    email = models.EmailField() 
    profesion = models.CharField(max_length=100)

#
#class Perfil(models.Model):
#    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
#    biografia = models.TextField(blank=True)
#    fecha_nacimiento = models.DateField(null=True, blank=True)
#    link = models.URLField(blank=True)
#
#    def __str__(self):
#        return f'Perfil de {self.usuario.username}'
#


from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


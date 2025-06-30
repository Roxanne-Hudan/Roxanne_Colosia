from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # Necesario si quieres saber quién publicó

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.post.titulo}"
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'usuario')  #Asi solo se puede dar una vez like

    def __str__(self):
        return f"{self.usuario.username} le dio like a {self.post.titulo}"


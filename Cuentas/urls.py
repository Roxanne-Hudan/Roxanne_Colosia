from django.urls import path
from AppCoder.views import login_request, register, editarPerfil, logout_request


urlpatterns = [
    path('', login_request, name='accounts_home'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('editar-perfil/', editarPerfil, name='editar_perfil'),
    path('logout/', logout_request, name='logout'),
]

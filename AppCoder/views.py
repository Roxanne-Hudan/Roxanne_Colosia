from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, EditProfileForm, AvatarForm, LoginForm
from .models import Avatar

from django.shortcuts import render

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def about(request):
    return render(request, 'AppCoder/about.html')

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return redirect('inicio')
    else:
        form = LoginForm()
    return render(request, 'AppCoder/usuario/login.html', {'form': form})

def logout_request(request):
    logout(request)
    return redirect('inicio')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Después de registrarse, va a login
    else:
        form = UserRegisterForm()
    return render(request, 'AppCoder/usuario/registro.html', {'form': form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Cambia a la url que quieras
    else:
        form = EditProfileForm(instance=usuario)
    return render(request, 'AppCoder/usuario/editarPerfil.html', {'form': form})

@login_required
def upload_avatar(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Cambia la url que necesites
    else:
        form = AvatarForm(instance=avatar)
    return render(request, 'AppCoder/usuario/upload_avatar.html', {'form': form})

from django.shortcuts import render
from AppCoder.forms import ProfesorFormulario
from AppCoder.models import Profesor


def leerProfesores (request):
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/formulario/leerProfesores.html", {"profesores": profesores})


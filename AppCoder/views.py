from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import CursoFormulario, ProfesorFormulario, EstudianteForm, EntregableForm, CursoForm
from django.http import HttpResponse

# Create your views here.

def lista_estudiantes(requets):
    estudiantes = Estudiante.objects.all()
    return render(requets, "estudiantes_list.html", {"estudiantes":estudiantes})

def detalle_estudiante(requets, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(requets, "estudiante_detail.html", {"estudiante":estudiante})

def inicio(request):
    return render(request, "AppCoder/index.html")

def cursos(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm()

    cursos = Curso.objects.all()
    return render(request, "AppCoder/cursos.html", {
        "form": form,
        "cursos": cursos
    })

def buscar(request):
    camada = request.GET.get('camada', None)
    cursos = []
    if camada:
        cursos = Curso.objects.filter(camada=camada)
    return render(request, 'AppCoder/resultados_busqueda.html', {'cursos': cursos, 'camada': camada})

def busqueda_camada(request):
    camada = request.GET.get("camada", "")
    cursos = Curso.objects.filter(camada=camada) if camada else []
    return render(request, "AppCoder/resultados_busqueda.html", {"cursos": cursos, "camada": camada})

def profesores(request):
    if request.method == "POST":
        informacion = request.POST
        profesor = Profesor(
            nombre=informacion['nombre'],
            apellido=informacion['apellido'],
            email=informacion['email'],
            profesion=informacion['profesion']
        )
        profesor.save()
        return render(request, "AppCoder/profesores.html", {"mensaje": "Profesor agregado con éxito"})

    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiantes')  # Redirige para evitar reenvío del formulario
    else:
        form = EstudianteForm()

    estudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/estudiantes.html", {
        "form": form,
        "estudiantes": estudiantes
    })

def entregables(request):
    if request.method == "POST":
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entregables')
    else:
        form = EntregableForm()

    entregables = Entregable.objects.all()
    return render(request, "AppCoder/entregables.html", {
        "form": form,
        "entregables": entregables
    })

def App(request):
    return render(request, "AppCoder/App.html")

# def cursoFormulario(request):
#     return render(request, "AppCoder/formulario/cursoFormulario.html")

def cursoFormulario(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST["curso"],camada=(request.POST["camada"]))
        curso.save()
        return render(request, "AppCoder/index.html")
    return render(request, "AppCoder/formulario/cursoFormulario.html")

def cursoFormulario2(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"],camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()        
    
    return render(request, "AppCoder/formulario/cursoFormulario2.html", {"miFormulario": miFormulario})


def profesorFormulario(request):

    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)  # aquí llega toda la información del html
        if miFormulario.is_valid():  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor = Profesor(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                profesion=informacion['profesion']
            )
            profesor.save()
            return render(request, "AppCoder/index.html")  # Vuelvo al inicio o a donde quieran
    else:
        miFormulario = ProfesorFormulario()  # Formulario vacío para construir el html

    return render(request, "AppCoder/formulario/profesorFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request, "AppCoder/formulario/busquedaCamada.html")

# def buscar(request):
#     if request.GET["camada"]:
#         #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }"
#         camada = request.GET['camada']
#         # icontains es un filtro que se usa para buscar coincidencias en los campos de texto de la base de datos, 
#         # sin importar si las letras están en mayúsculas o minúsculas
#         cursos = Curso.objects.filter(camada__icontains=camada)
# 
#         return render(request, "AppCoder/formulario/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})
# 
#     else:
#         respuesta = "No enviaste datos"
# 
#         # No olvidar from django.http import HttpResponse
#         return HttpResponse(respuesta)
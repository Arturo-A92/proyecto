from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from web_site.models import Curso
from web_site.forms import Busqueda, formulario


def home(request):
    return render (request, "web_site/home.html",{})

def cursoFormulario(request):

    if request.method == 'POST':

        miFormulario = formulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])

            curso.save()

            return render(request, "web_site/home.html")
        
    else:

        miFormulario= formulario()

        return render(request, "web_site/formulario.html", {"miFormulario":miFormulario})


def busqueda(request):

    return render(request, "web_site/busqueda.html")

def buscar(request):

    if request.GET["nombre"]:
        nombre =request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, "web_site/buscar.html", {"cursos":cursos, "nombre":nombre})

    else:
        respuesta = "no enviaste datos"

    return HttpResponse(respuesta)


def borrar(request):

    curso = Curso.objects.GET(nombre=request)
    curso.delete()

    cursos = Curso.objects.all()

    context= {"curso": curso}

    return render(request, "web_site/home.html", context)

def view(request):
    
    nombres = Curso.objects.all()

    context = {"nombres":nombres}

    return render(request, "web_site/views.html", context)













    

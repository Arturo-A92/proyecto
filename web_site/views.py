from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from web_site.models import Curso
from web_site.forms import formulario


def mostrar_index(request):
    return render (request, "web_site/index_nuevo.html", {})
    
def index(request):
    return render (request, "web_site/nuevo.html",{})

def home(request):
    return render (request, "web_site/home.html",{})

def lista_curso(request):
    return render (request, "web_site/lista_cursos.html",{})

def cursoFormulario(request):

    if request.method == 'POST':

        miFormulario = formulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])

            curso.save()

            return render(request, "aplicacion/home.html")
        pass
    else:

        miFormulario= formulario()

        return render(request, "aplicacion/cursoformulario.html", {"miFormulario":miFormulario})


# Create your views here.


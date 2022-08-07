from django.contrib import admin
from django.urls import path
from web_site.views import( cursoFormulario, home, index, lista_curso, mostrar_index, index )

urlpatterns = [
    path('index/', mostrar_index),
    path('index_nuevo/', index),
    path('home/', home),
    path('lista_cursos/', lista_curso),
    path('formulario_curso/', cursoFormulario),

]
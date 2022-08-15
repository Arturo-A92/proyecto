from django.contrib import admin
from django.urls import path
from web_site.views import( borrar, buscar, busqueda, cursoFormulario, home)
from web_site import views
urlpatterns = [
    path('home/', home),
    path('formulario/', cursoFormulario, name= "formulario"),
    path('eliminar/', borrar),
    path('busqueda/',views.busqueda, name= "busqueda"),
    path('busqueda/buscar/', views.buscar),
    path('views/',views.view),
    path('borrar/<nombre1>', views.borrar, name="borrar"),
    path('editar/<nombre1>', views.editar_nombre, name="editar")

]
from django.contrib import admin
from django.urls import path
from web_site.views import( borrar, buscar, busqueda, cursoFormulario, home)
from web_site import views
urlpatterns = [
    path('home/', home),
    path('formulario/', cursoFormulario),
    path('eliminar/', borrar),
    path('busqueda/',views.busqueda, name= "busqueda"),
    path('busqueda/buscar/', views.buscar),
    path('views/',views.view),

]
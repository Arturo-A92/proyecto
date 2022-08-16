from django.contrib import admin
from web_site.forms import formulario , Busqueda, UserRegisterform, meta 
from web_site.models import Curso, BlogModel, Avatar

admin.site.register(Curso)
admin.site.register(BlogModel)
admin.site.register(Avatar)
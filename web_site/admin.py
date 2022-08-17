from django.contrib import admin
from web_site.forms import formulario , Busqueda, UserRegisterform, meta 
from web_site.models import BlogModel, Avatar

admin.site.register(BlogModel)
admin.site.register(Avatar)
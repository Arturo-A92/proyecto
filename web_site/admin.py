from django.contrib import admin
from web_site.forms import Busqueda, UserRegisterform, meta 
from web_site.models import BlogModel, Publisher

admin.site.register(BlogModel)
admin.site.register(Publisher)

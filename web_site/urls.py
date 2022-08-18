from django.contrib import admin
from django.urls import path
from web_site.views import(buscar, busqueda, imagen, About)
from web_site import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('busqueda/',views.busqueda, name= "busqueda"),
    path('busqueda/buscar/', views.buscar),
    path('quienes_somos/', views.About),

#loggin
    path("crear/", views.SignUpView.as_view(), name ="blogger_signup"),
    path("profile/<pk>/", views.BloggerProfile.as_view(), name ="user-detail"),
    path("editar/<pk>/", views.UserUpdate.as_view(), name ="User-update"),

#blog
    path("", views.BlogList.as_view(), name="blog_list"),
    path("crearblog/", views.BlogCreate.as_view(), name="blog_create"),
    path("detalle/<pk>/", views.BlogDetail.as_view(), name ="blog_detail"),
    path("editarblog/<pk>/", views.BlogUpdate.as_view(), name ="blog_update"),
    path("borrar/<pk>/", views.BlogDelete.as_view(), name ="blog_delete"),
    path("entrar/", views.BlogLogin.as_view(), name="blog_login"),
    path("salir/", views.BlogLogout.as_view(), name="blog_logout"),

    
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




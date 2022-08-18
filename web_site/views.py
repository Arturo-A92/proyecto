from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from django.views.generic import ListView, TemplateView, View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from web_site.models import BlogModel, Publisher
from web_site.forms import Busqueda


def busqueda(request):

    return render(request, "web_site/busqueda.html")

def buscar(request):

    if request.GET["nombre"]:
        nombre =request.GET['nombre']
        blogs = BlogModel.objects.filter(titulo__icontains=nombre)
        return render(request, "web_site/buscar.html", {"blogs":blogs, "titulo":nombre})

    else:
        respuesta = "no enviaste datos"

    return HttpResponse(respuesta)

def imagen(request):
        avatares= BlogModel.objects.filter(user=request.user.id)
        return render(request, "web_site/inicio.html", {"url":avatares[0].imagen.url})

def About(request):
    return render(request, "web_site/about.html")


#loggin

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'web_site/blogger_crear_cuenta_form.html'
  success_url = reverse_lazy('blog_login')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

class BloggerProfile(DetailView):

    model = Publisher
    template_name = "web_site/blogger_detail.html"

class UserUpdate(LoginRequiredMixin, UpdateView):

    model = User
    template_name = "web_site/user_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
      return reverse_lazy("user-detail", kwargs={"pk": self.request.user.id})

#blog

class BlogList(ListView):

    model = BlogModel
    template_name = "web_site/inicio.html"
    

class BlogDetail(DetailView):

    model = BlogModel
    template_name = "web_site/detalles.html"


class BlogCreate(LoginRequiredMixin, CreateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class BlogUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo"]

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False
        


class BlogDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False


class BlogLogin(LoginView):
    template_name = 'web_site/logueo.html'
    next_page = reverse_lazy("blog_list")


class BlogLogout(LogoutView):
    template_name = 'web_site/cerrar_sesion.html'




    

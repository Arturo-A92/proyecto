from django import forms

class formulario(forms.Form):

    curso = forms.CharField(required = True )
    camada = forms.IntegerField()

class Busqueda(forms.Form):
    criterio = forms.CharField()

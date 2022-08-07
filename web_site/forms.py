from django import forms

class formulario(forms.Form):

    curso = forms.CharField(required = True )
    camada = forms.IntegerField()


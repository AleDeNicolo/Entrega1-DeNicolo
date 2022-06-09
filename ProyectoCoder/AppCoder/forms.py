from django import forms

class ServiceFormulario(forms.Form):
    service = forms.CharField(max_length=50)
    chasis = forms.IntegerField()


class MecanicosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=40)
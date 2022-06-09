from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Service, Mecanicos, Cliente
from django.template import loader
from AppCoder.forms import ServiceFormulario, MecanicosFormulario


# Create your views here.


def mecanicos (request):
    return render(request, "AppCoder/mecanicos.html")
    

def service (request):
    return render(request, "AppCoder/service.html")
   

def cliente (request):
    return render(request, "AppCoder/cliente.html")
    

def entregables (request):
    return render(request, "AppCoder/entregables.html")
    

def inicio(self):
    plantilla = loader.get_template("AppCoder/inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def serviceFormulario(request):
    if request.method == "POST":
        miFormulario = ServiceFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion["service"]
        chasis = informacion["chasis"]
        service = Service(nombre=nombre, chasis=chasis)
        service.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ServiceFormulario()
    return render (request, "AppCoder/serviceFormulario.html", {"miFormulario":miFormulario})

def mecanicosFormulario(request):
    if request.method == "POST":
        miFormulario = MecanicosFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion["nombre"]
        apellido = informacion["apellido"]
        email = informacion["email"]
        especialidad = informacion["especialidad"]
        mecanicos = Mecanicos(nombre=nombre, apellido=apellido, email=email, especialidad=especialidad)
        mecanicos.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = MecanicosFormulario()
    return render (request, "AppCoder/mecanicosFormulario.html", {"miFormulario":miFormulario})

def busquedaChasis(request):
    return render(request, "AppCoder/busquedaChasis.html")

def buscar(request):

    if request.GET['chasis']:
        chasis = request.GET['chasis']
        service = Service.objects.filter(chasis=chasis)
        return render (request, 'AppCoder/resultadosBusqueda.html', {'service':service, 'chasis':chasis} )
    else:
        respuesta = "No se ha ingresado un dato Valido"
    return HttpResponse(respuesta)


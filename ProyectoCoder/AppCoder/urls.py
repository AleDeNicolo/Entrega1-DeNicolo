from django.urls import path
from AppCoder.views import mecanicos, inicio, service, cliente, entregables, serviceFormulario, mecanicosFormulario,busquedaChasis, buscar



urlpatterns = [
    
    path("mecanicos/", mecanicos, name= "Mecanicos"),
    path("service/", service, name= "Service"),
    path("cliente/", cliente, name= "Cliente"),
    path("entregables/", entregables, name= "Entregables"),
    path("serviceFormulario/", serviceFormulario, name= "ServiceFormulario"),
    path("mecanicosFormulario/", mecanicosFormulario, name= "MecanicosFormulario"),
    path("busquedaChasis/", busquedaChasis, name= "BusquedaChasis"),
    path("buscar/", buscar, name= "Buscar"),
    path("", inicio, name= "Inicio"),
]         


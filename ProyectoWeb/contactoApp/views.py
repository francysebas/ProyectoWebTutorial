from django.shortcuts import render
from .forms import FormularioContactos
# Create your views here.


def contacto(request):
    # instanciar el formulario
    formulario_contacto = FormularioContactos()

    return render(request, "contactoApp/contacto.html", {'miFormularioContacto': formulario_contacto})


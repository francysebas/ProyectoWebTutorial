from django.shortcuts import render
from AppServicios.models import Servicio


# Create your views here.

def servicio(request):
    servicios = Servicio.objects.all()
    return render(request, "AppServicios/servicio.html", {"servicios": servicios})

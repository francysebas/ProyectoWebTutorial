from django.shortcuts import render
# from AppServicios.models import Servicio


# Create your views here.


def home(request):
    # return HttpResponse("Inicio...")
    return render(request, "ProyectoWebApp/home.html")


''' 
def servicio(request):
    servicios = Servicio.objects.all()
    return render(request, "ProyectoWebApp/servicio.html", {"servicios": servicios})
'''

'''
def blog(request):
    return render(request, "ProyectoWebApp/blog.html")
'''


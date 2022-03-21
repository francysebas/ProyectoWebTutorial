from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    # return HttpResponse("Inicio...")
    return render(request, "ProyectoWebApp/home.html/")


def servicio(request):
    return render(request, "ProyectoWebApp/servicio.html/")


def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html/")


def blog(request):
    return render(request, "ProyectoWebApp/blog.html/")


def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html/")

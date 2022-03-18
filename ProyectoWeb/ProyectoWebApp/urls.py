from django.urls import path

from ProyectoWebApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('servicio/', views.servicio, name="Servicio"),
    path('tienda/', views.tienda, name="tienda"),
    path('blog/', views.blog, name="Blog"),
    path('contacto/', views.contacto, name="Contacto"),
]
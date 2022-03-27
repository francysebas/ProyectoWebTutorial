from django.urls import path
from . import views

app_name = "carro"

urlpatterns = [

    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_prodto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_prodto, name="restar"),
    path("limpiar/<int:producto_id>/", views.limpiar_carro, name="limpiar"),


]
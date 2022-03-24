from django.db import models


# Create your models here.


class CategoriaProducto(models.Model):
    nombreCat = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoriaProducto'
        verbose_name_plural = 'categoriasProductos'

    def __str__(self):
        return self.nombreCat


class Producto(models.Model):
    nombreProd = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tiendaApp', null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombreProd


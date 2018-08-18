from django.db import models


class UnidadesDeMedida(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return 'Unidad {} lalalal'.format(self.nombre)

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return 'Tipo {}'.format(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.SET_NULL, null=True)
    unidad_de_medida = models.ForeignKey(UnidadesDeMedida, on_delete=models.CASCADE)

    fecha_ultima_compra = models.DateField(null=True, blank=True)

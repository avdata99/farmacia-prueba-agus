from django.contrib import admin
from .models import UnidadesDeMedida, TipoProducto, Producto

@admin.register(UnidadesDeMedida)
class UnidadesDeMedidaAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'unidad_de_medida']
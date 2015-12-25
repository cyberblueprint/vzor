from django.contrib import admin

from .models import Empresa, Producto, Productos, Licencia


# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ['pk', 'nombre']

class ProductoAdmin(admin.ModelAdmin):
	list_display = ['pk', 'producto']
	list_filter = ['producto']


class ProductosAdmin(admin.ModelAdmin):
	list_display = ['empresa_id', 'mostrar_productos']

	def mostrar_productos(self, obj):
		return "\n".join([a.producto for a in obj.productos.all()])


class LicenciaAdmin(admin.ModelAdmin):
	date_hierarchy = 'inicio'
	search_fields = ['inicio', 'fin']
	list_display = ['pk', 'usuario', 'numero_de_monitores', 'numero_de_pasos', 'token', 'inicio', 'fin', 'habilitado', 'producto_id']
	list_filter = ['numero_de_monitores', 'habilitado']
	list_editable = ['habilitado']

	def mostrar_empresa(self, obj):
		return "\n".join([a.empresa for a in obj.empresa.all()])



admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Licencia, LicenciaAdmin)

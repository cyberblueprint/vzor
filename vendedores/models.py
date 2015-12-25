from django.db import models
from django.contrib.auth.models import User

from datetime import *

# Create your models here.
class Empresa(models.Model):
	nombre = models.CharField(max_length=300)
	datos_generales = models.TextField()

	def __str__(self):
		return self.nombre


PRODUCTOS = (
	('1', 'vzor_suite'),
	('2', 'vzor_cloud'),
)

class Producto(models.Model):
	producto = models.CharField(max_length=300, choices=PRODUCTOS)

	def __str__(self):
		return "{}".format(self.producto)


class Productos(models.Model):
	empresa_id = models.ForeignKey(Empresa)
	productos = models.ManyToManyField(Producto, related_name="productos_todos")

	def __str__(self):
		return "{}".format(self.productos)

class Licencia(models.Model):
	usuario = models.ForeignKey(User)
	empresa = models.OneToOneField(Empresa, primary_key=True)
	numero_de_monitores = models.IntegerField()
	numero_de_pasos = models.IntegerField()
	token = models.DateTimeField()
	inicio = models.DateTimeField(auto_now_add=True)
	fin = models.DateTimeField()
	habilitado = models.BooleanField()
	producto_id = models.OneToOneField(Producto)
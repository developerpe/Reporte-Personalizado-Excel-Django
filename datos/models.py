from django.db import models

class Datos(models.Model):
	nombre = models.CharField(max_length = 255, blank = False,null = False)
	edad = models.IntegerField()
	apellidos = models.CharField(max_length = 255, blank = False,null = False)
	direccion = models.CharField(max_length = 255, blank = False,null = False)

	class Meta:
		verbose_name = 'Dato'
		verbose_name_plural = 'Datos'

	def __str__(self):
		return self.nombre

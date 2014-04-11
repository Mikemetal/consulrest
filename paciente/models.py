from django.db import models

class Paciente(models.Model):
	nombre = models.CharField(max_length=50)
	fechacreacion = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.Nombre

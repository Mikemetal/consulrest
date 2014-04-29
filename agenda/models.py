from django.db import models
from paciente.models import Paciente

# Create your models here.
class Agenda(models.Model):
	paciente = models.ForeignKey(Paciente, related_name='paciente',null=True)
	descripcion = models.CharField(max_length=50)
	fecha = models.DateField()
	horainicio = models.TimeField()
	horafinal = models.TimeField()
	asistio = models.BooleanField()
	cancelada = models.BooleanField()

	def __unicode__(self):
		return self.descripcion
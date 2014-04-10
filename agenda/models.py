from django.db import models
from paciente.models import Paciente

# Create your models here.
class Agenda(models.Model):
	PacienteID = models.ForeignKey(Paciente)
	Descripcion = models.CharField(max_length=50)
	Fecha = models.DateField()
	HoraInicio = models.TimeField()
	HoraFinal = models.TimeField()
	Asistio = models.BooleanField()
	Cancelada = models.BooleanField()

	def __unicode__(self):
		return self.Descripcion
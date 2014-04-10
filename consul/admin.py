from django.contrib import admin
from agenda.models import Agenda
from paciente.models import Paciente

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('Descripcion', 'Fecha', 'HoraInicio', 'HoraFinal','Asistio','Cancelada')
  #  filter_vertical = ('Fecha',)
 #   actions = [export_as_csv]
 #   inlines = [EnlaceInline]

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'FechaCreacion')
  #  filter_vertical = ('Nombre',)

admin.site.register(Agenda,AgendaAdmin)
admin.site.register(Paciente,PacienteAdmin)
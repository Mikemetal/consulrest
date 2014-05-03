from django.contrib import admin
from agenda.models import Agenda
from paciente.models import Paciente

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('paciente','descripcion', 'fecha', 'horainicio', 'horafinal','asistio','cancelada','usuario')

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fechacreacion')

admin.site.register(Agenda,AgendaAdmin)
admin.site.register(Paciente,PacienteAdmin)
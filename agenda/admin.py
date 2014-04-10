from django.contrib import admin
from agenda.models import Agenda

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('Descripcion', 'Fecha', 'HoraInicio', 'HoraFinal','Asistio','Cancelada')
  #  filter_vertical = ('Fecha',)
 #   actions = [export_as_csv]
 #   inlines = [EnlaceInline]

admin.site.register(Agenda,AgendaAdmin)
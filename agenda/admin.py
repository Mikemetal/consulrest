from django.contrib import admin
from agenda.models import Agenda

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'fecha', 'horainicio', 'horafinal','asistio','cancelada')
  #  filter_vertical = ('Fecha',)
 #   actions = [export_as_csv]
 #   inlines = [EnlaceInline]

admin.site.register(Agenda,AgendaAdmin)
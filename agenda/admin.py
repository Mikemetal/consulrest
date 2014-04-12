from django.contrib import admin
from agenda.models import Agenda

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'fecha', 'horainicio', 'horafinal','asistio','cancelada')

admin.site.register(Agenda,AgendaAdmin)
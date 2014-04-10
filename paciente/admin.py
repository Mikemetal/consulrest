from django.contrib import admin
from paciente.models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'FechaCreacion')
  #  filter_vertical = ('Nombre',)


admin.site.register(Paciente,PacienteAdmin)
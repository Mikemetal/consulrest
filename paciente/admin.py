from django.contrib import admin
from paciente.models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fechacreacion')
  #  filter_vertical = ('Nombre',)


admin.site.register(Paciente,PacienteAdmin)
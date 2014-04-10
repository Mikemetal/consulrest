#from django.forms import widgets
from rest_framework import serializers
#from django.contrib.auth.models import User
from agenda.models import Agenda


class AgendaSerializer(serializers.ModelSerializer):
    #owner = serializers.Field(source='owner.username')
    class Meta:
        model = Agenda
        fields = ('id','Descripcion', 'Fecha', 'HoraInicio', 'HoraFinal', 'Asistio','Cancelada')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
           # instance.Paciente = attrs.get('Paciente', instance.Paciente)
            instance.Descripcion = attrs.get('Descripcion', instance.Descripcion)
            instance.Fecha = attrs.get('Fecha', instance.Fecha)
            instance.HoraInicio = attrs.get('HoraInicio', instance.HoraInicio)
            instance.HoraFinal = attrs.get('HoraFinal', instance.HoraFinal)
            instance.Asistio = attrs.get('Asistio', instance.Asistio)
            instance.Cancelada = attrs.get('Cancelada', instance.Cancelada)
            return instance

        # Create new instance
        return Agenda(**attrs)
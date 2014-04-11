#from django.forms import widgets
from rest_framework import serializers
#from django.contrib.auth.models import User
from agenda.models import Agenda


class AgendaSerializer(serializers.ModelSerializer):
    #owner = serializers.Field(source='owner.username')
    paciente = serializers.RelatedField(many=False)
    class Meta:
        model = Agenda
        fields = ('id','paciente','descripcion', 'fecha', 'horainicio', 'horafinal', 'asistio','cancelada')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.paciente = attrs.get('paciente', instance.paciente)
            instance.descripcion = attrs.get('descripcion', instance.descripcion)
            instance.fecha = attrs.get('fecha', instance.fecha)
            instance.horainicio = attrs.get('horainicio', instance.horainicio)
            instance.horafinal = attrs.get('horafinal', instance.horafinal)
            instance.asistio = attrs.get('asistio', instance.asistio)
            instance.cancelada = attrs.get('cancelada', instance.cancelada)
            return instance

        # Create new instance
        return Agenda(**attrs)
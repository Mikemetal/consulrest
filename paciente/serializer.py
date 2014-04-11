#from django.forms import widgets
from rest_framework import serializers
#from django.contrib.auth.models import User
from paciente.models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    #owner = serializers.Field(source='owner.username')
    class Meta:
        model = Paciente
        fields = ('id', 'nombre', 'fechacreacion')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.nombre = attrs.get('nombre', instance.nombre)
            instance.fechacreacion = attrs.get('fechacreacion', instance.fechacreacion)
            return instance

        # Create new instance
        return Paciente(**attrs)
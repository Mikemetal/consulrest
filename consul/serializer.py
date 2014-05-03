#from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    #owner = serializers.Field(source='owner.username')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.username = attrs.get('username', instance.username)
            instance.first_name = attrs.get('first_name', instance.first_name)
            instance.last_name = attrs.get('last_name', instance.last_name)
            instance.name = attrs.get('name', instance.name)
            return instance

        # Create new instance
        return User(**attrs)
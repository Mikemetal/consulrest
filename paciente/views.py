#from rest_framework import mixins
from django.contrib.auth.models import User
from rest_framework import generics
from paciente.models import Paciente
from paciente.serializer import PacienteSerializer
from rest_framework import permissions
#from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class PacienteList(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #def pre_save(self, obj):
    #    obj.owner = self.request.user


class PacienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    # def pre_save(self, obj):
    #     obj.owner = self.request.user
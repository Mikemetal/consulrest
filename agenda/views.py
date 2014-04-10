#from rest_framework import mixins
from django.contrib.auth.models import User
from rest_framework import generics
from agenda.models import Agenda
from agenda.serializer import AgendaSerializer
from rest_framework import permissions
#from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class AgendaList(generics.ListCreateAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #def pre_save(self, obj):
    #    obj.owner = self.request.user


class AgendaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    # def pre_save(self, obj):
    #     obj.owner = self.request.user
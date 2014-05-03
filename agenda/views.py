from rest_framework import generics
from agenda.models import Agenda
from agenda.serializer import AgendaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date


class AgendaList(generics.ListCreateAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.usuario = self.request.user


class AgendaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.usuario = self.request.user


class AgendaHoy(APIView):
    def get(self, request, format=None):
        agendahoy = Agenda.objects.filter(fecha=date.today(), usuario = request.user)
        print(agendahoy)
        print(agendahoy)
        serializer = AgendaSerializer(agendahoy, many=True)
        return Response(serializer.data)

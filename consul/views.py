from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from consul.serializer import UserSerializer
from rest_framework.response import Response

@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class obtener_datos_usuario(APIView):
    def get(self,request):
        usuario = Token.objects.get( key = request.META['HTTP_AUTHORIZATION'].replace("Token ",""))
        datosusuario = User.objects.filter(username = usuario.user)
        serializer = UserSerializer(datosusuario, many=True)
        return Response(serializer.data)


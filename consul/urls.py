from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from consul import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^obtenerusuario/$', views.obtener_datos_usuario.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
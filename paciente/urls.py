from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from paciente import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^paciente/$', views.PacienteList.as_view()),
    url(r'^paciente/(?P<pk>[0-9]+)/$', views.PacienteDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
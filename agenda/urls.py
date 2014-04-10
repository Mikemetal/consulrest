from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from agenda import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^agenda/$', views.AgendaList.as_view()),
    url(r'^agenda/(?P<pk>[0-9]+)/$', views.AgendaDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
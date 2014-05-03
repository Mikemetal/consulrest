from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'debin_consul.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^', include('agenda.urls')),
    url(r'^', include('paciente.urls')),
    url(r'^', include('consul.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),

)
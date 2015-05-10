from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^v1/f5/cookie/decode', 'api.f5.cookie.views.decode', name='f5-cookie-decode'),
    url(r'^admin/', include(admin.site.urls)),
)

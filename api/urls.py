from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^v1/f5/cookie/decode', 'api.f5.cookie.views.decode', name='f5-cookie-decode'),
    # url(r'^v1/f5/cookie/encode', 'api.f5.cookie.views.encode', name='f5-cookie-encode'),
    url(r'^admin/', include(admin.site.urls)),
)

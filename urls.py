from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    
    (r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:-1], 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    (r'favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/media/favicon.ico'}),
    
    (r'(?P<slug>(.*))', 'geostatic.views.main' ),

)

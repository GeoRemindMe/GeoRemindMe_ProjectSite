from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    
    
    (r'^admin/?', include(admin.site.urls)),
    (r'^survey/es/?', 'geostatic.views.set_language_es'),
    (r'^survey/en/?', 'geostatic.views.set_language_en'),
    (r'^ajax/contact/', 'geostatic.views.contact'),
    (r'^ajax/keep-up-to-date/', 'geostatic.views.keepuptodate'),
    (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:-1], 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    url(r'^lang/$', 'geostatic.views.set_language'),
    (r'favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/media/favicon.ico'}),
    
    (r'^update/?$', 'geostatic.views.update' ),
    
    (r'(?P<slug>(.*))$', 'geostatic.views.main' ),
    

)

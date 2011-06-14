# Create your views here.

from geostatic.models import Page
from django.shortcuts import get_object_or_404,render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import urlparse
import re


def main(request,slug=""):

    #if re.match(r'\w+.\w+.\w{1,3}',request.META['HTTP_HOST']):
    #if re.match(r'$\w+\.\w+\.\w{1,3}',request.META['HTTP_HOST']):
    if re.match(r'^\w+\.\w+\.\w{1,3}',request.META['HTTP_HOST']):
        subdomain = request.META['HTTP_HOST'].split('.')[0]
        
        if subdomain == "www":
            subdomain = ""
        
    else:
        subdomain = ""
       
    if slug and slug[-1]=="/":
		slug = slug[:-1]

    print 'Subdomain='+subdomain
    print 'Slug='+slug
    page = get_object_or_404(Page,slug=slug,subdomain=subdomain)
    

    return render_to_response(page.template, context_instance=RequestContext(request))

def set_language(request):
    if request.method == 'POST':
        from django.conf import settings
        available = dict(settings.LANGUAGES)
        lang = request.POST.get('lang', settings.LANGUAGE_CODE)
        next = request.POST.get('next', '/')
        if lang in available: #we have the lang_code
            request.session['LANGUAGE_CODE'] = lang
        
        return HttpResponseRedirect(next)
        
    return HttpResponseRedirect(request.path)    

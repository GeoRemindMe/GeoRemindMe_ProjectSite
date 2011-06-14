# Create your views here.

from geostatic.models import Page
from django.shortcuts import get_object_or_404,render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import urlparse
import re

def main(request,slug=""):


    if re.match(r'\w+.\w+.\w{1,3}',request.META['HTTP_HOST']):
        subdomain = request.META['HTTP_HOST'].split('.')[0]
        
        if subdomain == "www":
            subdomain = ""
        
    else:
        subdomain = ""

    page = get_object_or_404(Page,slug=slug,subdomain=subdomain)

    return render_to_response(page.template, context_instance=RequestContext(request))
    

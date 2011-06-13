# Create your views here.

from geostatic.models import Page
from django.shortcuts import get_object_or_404,render_to_response
from django.template import RequestContext
import urlparse

def main(request,slug=""):
    
    subdomain = urlparse.urlsplit(request.META['HTTP_HOST'])[0].split('.')
      
    page = get_object_or_404(Page,slug=slug,subdomain=subdomain)
    
    return render_to_response(page.template, context=RequestContext(request))
    

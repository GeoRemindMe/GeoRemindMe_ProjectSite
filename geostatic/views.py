from geostatic.models import Page
from django.shortcuts import get_object_or_404,render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.core.mail import send_mail


import urlparse
import re


from django.http import HttpResponseBadRequest
def ajax_request(func):
    def _wrapper(*args, **kwargs):
        request = args[0]
        if request.method <> "POST" or not request.is_ajax():
            return HttpResponseBadRequest("Not AJAX or POST", mimetype="text/plain")
        return func(*args, **kwargs)
    return _wrapper

@ajax_request
def contact(request):
        
    send_mail('Formulario de contacto', request.POST.get('msg',''), request.POST.get('userEmail',''),
    ['info@georemindme.com'], fail_silently=False)
    
    return HttpResponse()

@ajax_request
def keepuptodate(request):    
    data = ''
    for k in request.POST.keys():
        if k.endswith("version"):
            data+=(k+"<br/>")

    
    send_mail('Usuario quiere recibir novedades', data, request.POST.get('user-email',''),
    ['info@georemindme.com'], fail_silently=False)
    
    return HttpResponse()

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

    #print 'Subdomain='+subdomain
    #print 'Slug='+slug
    page = get_object_or_404(Page,slug=slug,subdomain=subdomain)
    

    return render_to_response(page.template, context_instance=RequestContext(request))
    
def update(request):
    from django.conf import settings
    import subprocess

    proc = subprocess.Popen(settings.UPDATE_SCRIPT, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

    stdout,stderr = proc.communicate()

    return HttpResponse(stdout+"\n\n"+stderr,mimetype="text/plain")

def set_language(request):
  if request.method == 'POST':
      from django.conf import settings
      available = dict(settings.LANGUAGES)
      lang = request.POST.get('lang', settings.LANGUAGE_CODE)
      next = request.POST.get('next', '/')
      if lang in available: #we have the lang_code
          from django.utils import translation
          #request.session['LANGUAGE_CODE'] = lang
          request.session["django_language"] = lang
          translation.activate(lang)
          request.LANGUAGE_CODE = translation.get_language()
      
      
          return HttpResponseRedirect(next)
      return HttpResponseRedirect(request.path)
    
    
def set_language_es(request):
  from django.conf import settings
  available = dict(settings.LANGUAGES)
  lang = 'es'
  next = '/survey/'
  from django.utils import translation
  request.session["django_language"] = lang
  translation.activate(lang)
  request.LANGUAGE_CODE = translation.get_language()
 
  return HttpResponseRedirect(next)


def set_language_en(request):
  from django.conf import settings
  available = dict(settings.LANGUAGES)
  lang = 'en'
  next = '/survey/'
  from django.utils import translation
  request.session["django_language"] = lang
  translation.activate(lang)
  request.LANGUAGE_CODE = translation.get_language()

  return HttpResponseRedirect(next)


#!/usr/bin/env python
# -*- coding: utf-8 -*-


from os import path
from settings import LANGUAGES
BASE_DIR = path.normpath(path.dirname(__file__))

''' 
A locale name, either a language specification of the form ll or a 
combined language and country specification of the form ll_CC. 
Examples: it, de_AT, es, pt_BR. 

Note the underscore in some of them and the case of the part located 
to its right.

#List supported languages
On Ubuntu: cat /usr/share/i18n/SUPPORTED

#More info about language tags
RFC 5646: http://www.rfc-editor.org/rfc/rfc5646.txt
LANGTAG: http://www.langtag.net
W3C: http://www.w3.org/International
'''


import commands

for lang in LANGUAGES:
	if commands.getstatusoutput('django-admin makemessages -l '+lang[0])[0]==0:#creates german (de) .po
		print lang[1] + ' strings updated at \'locale/'+lang[0]+'/LC_MESSAGES/django.po\''
	elif commands.getstatusoutput('django-admin.py makemessages -l '+lang[0])[0]==0:#creates german (de) .po
		print lang[1] + ' strings updated at \'locale/'+lang[0]+'/LC_MESSAGES/django.po\''
	else:
		print lang[1] + ' strings couldn\'t be updated at \'locale/'+lang[0]+'/LC_MESSAGES/django.po\''
		
print 'Now look if there is any translation tagged with #fuzzy or without been translated'
		

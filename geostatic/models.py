# coding=utf-8

from django.db import models
from django.contrib.sites.models import Site

class Page(models.Model):
    slug = models.SlugField("Slug",blank=True,help_text=u"Blank for root url")
    subdomain = models.CharField("Subdomain",max_length=255,blank=True,help_text=u"Blank for www (equal to no subdomain)")
    template = models.CharField("Template",max_length=255)
    
    def __unicode__(self):
        return unicode(self.slug)+u" on "+unicode(self.subdomain)
    
    class Meta:
        verbose_name = "page"
        unique_together = ('slug','subdomain',)

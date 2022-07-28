from django.db import models

# Create your models here.
class Crm(models.Model):
    phone = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    fax = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    lead_type = models.CharField(max_length=200, null=True, blank=True)
    market_segment = models.CharField(max_length=200, null=True, blank=True)
    industry = models.CharField(max_length=200, null=True, blank=True)
    request_type = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    territory = models.CharField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=200, null=True, blank=True)
    subscribed = models.CharField(max_length=200, null=True, blank=True)
    blog_subscribed = models.CharField(max_length=200, null=True, blank=True)
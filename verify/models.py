# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Verify(models.Model):
    path = models.CharField(primary_key=True, max_length=255)
    status = models.CharField(max_length=255)
    tab = models.CharField(max_length=255, blank=True, null=True)
    check = models.CharField(max_length=255, blank=True, null=True)
    uptime = models.CharField(max_length=255,blank=True, null=True)
    expiretime = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    checker = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verify'

# class Verify(models.Model):
#     path = models.CharField(unique=True, max_length=255, blank=True, null=True)
#     status = models.CharField(max_length=255, blank=True, null=True)
#     tab = models.CharField(max_length=255, blank=True, null=True)
#     verify = models.CharField(max_length=255, blank=True, null=True)
#     uptime = models.CharField(max_length=255, blank=True, null=True)
#     operator = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'verify'

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class VCinfo(models.Model):
    hostname = models.CharField(max_length=17)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    vmname = models.CharField(max_length=100)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Testdata(models.Model):
    def __init__(self):
        self.text = models.CharField(max_length=50)
        self.val = models.IntegerField()
    def __str__(self):
        return self.text

class VcenterInfo(models.Model):
    def __init__(self):
        self.ipaddr = models.CharField(max_length=17)
        self.user = models.CharField(max_length=100)
        self.passwd = models.CharField(max_length=100)
        self.vmname = models.CharField(max_length=100)
    def __str__(self):
        return self.ipaddr
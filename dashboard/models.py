# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class VMInfo(models.Model):
    def __init__(self):
        self.text = models.CharField(max_length=50)
        self.val = models.IntegerField()
    def __str__(self):
        return self.text
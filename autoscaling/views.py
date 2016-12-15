# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from .models import VcenterInfo

# Create your views here.
def autoscaling(request):
    if VcenterInfo:
        return render(request, "autoscaling.html", {'message':"welcome"})
    VcenterInfo()
    return render(request, "autoscaling.html", {'message': "please retry"})

def run_as(request):
    if 'ipaddr' in request.POST:
        ipaddr = request.POST['ipaddr']
    else:
        return render(request, "autoscaling.html")

    if 'user' in request.POST:
        user = request.POST['user']

    print request.POST['user']

    if 'passwd' in request.POST:
        password = request.POST['passwd']
    else:
        return render(request, "autoscaling.html")

    return render(request, "testresult.html", {"ipaddr":ipaddr, "user":user, "passwd":password})

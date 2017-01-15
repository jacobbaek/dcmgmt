# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from vcaform import VConnInput, VConnectInfo

# Create your views here.
def autoscaling(request):
    if request.method == 'POST':
        return redirect("/result")
    form = VConnInput(request.POST)
    return render(request, "autoscaling.html", {'form': form})

def result(request):
    return render(request, "result.html", {'vmname':VConnectInfo.vmname})
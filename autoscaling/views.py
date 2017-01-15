# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import VCinfo
from .vcaform import VCinfoForm

# Create your views here.
def autoscaling(request):
    if request.method == 'POST':
        form = VCinfoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/result")
    else:
        form = VCinfoForm()
    return render(request, "autoscaling.html", {'form': form})

def result(request, ):
    forms = VCinfo.objects.all()
    return render(request, "result.html", {'forms': forms})

def decrease(request):
    return render(request, "after_as.html", {'msg': 'decrease succeed'})

def increase(request):
    return render(request, "after_as.html", {'msg': 'increase succeed'})

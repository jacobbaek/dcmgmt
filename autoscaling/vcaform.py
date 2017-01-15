from django import forms
from .models import VCinfo

class VCinfoForm(forms.ModelForm):
    class Meta:
        model = VCinfo
        fields = ["hostname", "username", "password", "vmname"]
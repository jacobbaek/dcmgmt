from django import forms
from .models import VConnectInfo

class VConnInput(forms.ModelForm):
    class Meta:
        model = VConnectInfo
        fields = ("hostname", "username", "password", "vmname",)
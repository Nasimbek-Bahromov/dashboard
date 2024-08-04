from django import forms
from main.models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['address', 'phone', 'email']

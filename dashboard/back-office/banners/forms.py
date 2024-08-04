from django import forms
from main.models import Banner

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['title', 'sub_title', 'image', 'is_active']

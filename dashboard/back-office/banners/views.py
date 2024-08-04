from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from main.models import Banner
from . import forms


class BannerListView(ListView):
    model = Banner
    template_name = 'dashboard/back-office/banners/banner_list.html'
    context_object_name = 'banners'

class BannerCreateView(CreateView):
    model = Banner
    form_class = forms.BannerForm
    template_name = 'dashboard/back-office/banners/banner_update.html'
    success_url = reverse_lazy('banner_list')

class BannerUpdateView(UpdateView):
    model = Banner
    form_class = forms.BannerForm
    template_name = 'dashboard/back-office/banners/banner_update.html'
    success_url = reverse_lazy('banner_list')

class BannerDeleteView(DeleteView):
    model = Banner
    template_name = 'dashboard/back-office/banners/banner_delete.html'
    success_url = reverse_lazy('banner_list')

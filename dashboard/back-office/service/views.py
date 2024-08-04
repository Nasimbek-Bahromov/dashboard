from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from main.models import Service
from .forms import ServiceForm


class ServiceListView(ListView):
    model = Service
    template_name = 'dashboard/back-office/service/service_list.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'dashboard/back-office/service/service_detail.html'
    context_object_name = 'service'


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'dashboard/back-office/service/service_create.html'
    success_url = reverse_lazy('service_list')


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'dashboard/back-office/service/service_update.html'
    success_url = reverse_lazy('service_list')


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'dashboard/back-office/service/service_delete.html'
    success_url = reverse_lazy('service_list')

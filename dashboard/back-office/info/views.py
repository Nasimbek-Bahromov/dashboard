from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.models import Info
from .forms import InfoForm

class InfoListView(ListView):
    model = Info
    template_name = 'dashboard/back-office/info/info_list.html'
    context_object_name = 'infos'

class InfoDetailView(DetailView):
    model = Info
    template_name = 'dashboard/back-office/info/info_detail.html'

class InfoCreateView(CreateView):
    model = Info
    form_class = InfoForm
    template_name = 'dashboard/back-office/info/info_update.html'
    success_url = reverse_lazy('info_list')
    extra_context = {'form_title': 'Add New Info'}

class InfoUpdateView(UpdateView):
    model = Info
    form_class = InfoForm
    template_name = 'dashboard/back-office/info/info_update.html'
    success_url = reverse_lazy('info_list')
    extra_context = {'form_title': 'Edit Info'}

class InfoDeleteView(DeleteView):
    model = Info
    template_name = 'dashboard/back-office/info/info_delete.html'
    success_url = reverse_lazy('info_list')

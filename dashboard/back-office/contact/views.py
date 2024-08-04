from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.models import Contact
from .forms import ContactForm

class ContactListView(ListView):
    model = Contact
    template_name = 'dashboard/back-office/contact/contact_list.html'
    context_object_name = 'contacts'

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'dashboard/back-office/contact/contact_detail.html'

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'dashboard/back-office/contact/contact_update.html'
    success_url = reverse_lazy('contact_list')
    extra_context = {'form_title': 'Add New Contact'}

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'dashboard/back-office/contact/contact_update.html'
    success_url = reverse_lazy('contact_list')
    extra_context = {'form_title': 'Edit Contact'}

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'dashboard/back-office/contact/contact_delete.html'
    success_url = reverse_lazy('contact_list')

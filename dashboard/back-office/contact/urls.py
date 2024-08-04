from django.urls import path
from .views import ContactListView, ContactDetailView, ContactCreateView, ContactUpdateView, ContactDeleteView


urlpatterns = [
    path('list/', ContactListView.as_view(), name='contact_list'),
    path('detail/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('create/', ContactCreateView.as_view(), name='contact_create'),
    path('update/<int:pk>/', ContactUpdateView.as_view(), name='contact_update'),
    path('delete/<int:pk>/', ContactDeleteView.as_view(), name='contact_delete'),
]

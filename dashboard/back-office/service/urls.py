from django.urls import path
from .views import ServiceListView, ServiceDetailView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView

urlpatterns = [
    path('list/', ServiceListView.as_view(), name='service_list'),
    path('detail/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('create/', ServiceCreateView.as_view(), name='service_create'),
    path('update/<int:pk>/', ServiceUpdateView.as_view(), name='service_update'),
    path('delete/<int:pk>/', ServiceDeleteView.as_view(), name='service_delete'),
]

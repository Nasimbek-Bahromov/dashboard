from django.urls import path
from .views import InfoListView, InfoDetailView, InfoCreateView, InfoUpdateView, InfoDeleteView


urlpatterns = [
    path('info/', InfoListView.as_view(), name='info_list'),
    path('detail/<int:pk>/', InfoDetailView.as_view(), name='info_detail'),
    path('create/', InfoCreateView.as_view(), name='info_create'),
    path('update/<int:pk>', InfoUpdateView.as_view(), name='info_update'),
    path('delete/<int:pk>/', InfoDeleteView.as_view(), name='info_delete'),
]

from django.urls import path
from .views import BannerListView, BannerCreateView, BannerUpdateView, BannerDeleteView

urlpatterns = [
    path('list/', BannerListView.as_view(), name='banner_list'),
    path('create/', BannerCreateView.as_view(), name='banner_create'),
    path('update/<int:pk>/', BannerUpdateView.as_view(), name='banner_update'),
    path('delete/<int:pk>/', BannerDeleteView.as_view(), name='banner_delete'),
]

from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('back-office/', include('dashboard.back-office.urls')),
    path('', views.dashboard, name = 'dashboardIndex')
]
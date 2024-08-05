from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('back-office/', include('dashboard.back-office.urls')),
    path('authenticated/', include('dashboard.authenticated.urls')),
    path('', views.dashboard, name = 'dashboardIndex')
]
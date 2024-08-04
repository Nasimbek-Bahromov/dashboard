from django.urls import path, include

urlpatterns = [
    path('banners/', include('dashboard.back-office.banners.urls')),
    path('service/', include('dashboard.back-office.service.urls')),
    path('contact/', include('dashboard.back-office.contact.urls')),
    path('info/', include('dashboard.back-office.info.urls')),
]
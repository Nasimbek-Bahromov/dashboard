from django.shortcuts import render, redirect
from django.contrib import messages
from  main import models
 


def index(request):
    banners = models.Banner.objects.all()
    infos = models.Info.objects.last()
    contact = models.Contact.objects.all()
    services = models.Service.objects.all()




    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        models.Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )


    context = {
        'banners': banners,
        'infos': infos,
        'contact': contact,
        'services': services
    }

    return render(request, 'front/index.html', context)


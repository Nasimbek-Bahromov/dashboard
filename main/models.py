from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners/')
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    created = models.DateTimeField(auto_now_add=True)
    img_label = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()    

    def __str__(self):
        return self.name
    
    
class Info(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    
    

    

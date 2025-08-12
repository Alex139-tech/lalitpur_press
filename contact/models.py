from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
    
class Report(models.Model):
    name = models.CharField(max_length=150)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)   
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255)
    screenshot = models.ImageField(blank=True, null=True)
    aavedan = models.ImageField(blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.name

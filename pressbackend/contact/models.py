from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.name
    


# report model
class Report(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True,null=True)
    address = models.CharField(max_length=255)
    screenshot = models.ImageField(blank=True,null=True)
    aavedan = models.ImageField(blank=True,null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.name
    



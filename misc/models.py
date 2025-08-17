from django.db import models
# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)


class QR(models.Model):
    qr_image = models.ImageField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        get_latest_by = 'created_at'

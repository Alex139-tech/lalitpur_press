from django.contrib import admin
from .models import Publication,QR

# Register your models here.

  
@admin.register(Publication)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','published_date','file']  
    list_filter = ['title']


@admin.register(QR)
class QRAdmin(admin.ModelAdmin):
    list_display =  ['qr_image',]  

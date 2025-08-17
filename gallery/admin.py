from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import PhotoGallery, GalleryImage

class GalleryAdminForm(forms.ModelForm):
    class Meta:
        model = PhotoGallery
        fields = ['feature_image', 'title']


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3

     

@admin.register(PhotoGallery)
class GalleryAdmin(admin.ModelAdmin):
    form = GalleryAdminForm
    list_display = ('id', 'title')
    search_fields = ('title',)
    inlines = [GalleryImageInline]

     
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery')
    list_filter = ('gallery',)

    
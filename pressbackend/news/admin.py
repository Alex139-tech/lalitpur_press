from django.contrib import admin
from .models import News,Notice
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['image','title','content','status','created_at','published_date']


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['file','title','content','status','created_at','published_date']
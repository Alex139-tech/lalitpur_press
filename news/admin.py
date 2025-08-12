from django.contrib import admin
from django.utils.html import format_html
from .models import News, Notice


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'short_content', 'status', 'created_at', 'published_date')
    search_fields = ('title', 'content', 'status')
    list_filter = ('status', 'created_at', 'published_date')
    ordering = ('-created_at',)
    readonly_fields = ('image_preview', 'created_at', 'published_date')

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'content', 'status')
        }),
        ('Image', {
            'fields': ('image', 'image_preview')
        }),
        ('Dates', {
            'fields': ('created_at', 'published_date')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:80px; max-width:120px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"

    def short_content(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    short_content.short_description = "Content"


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('file_link', 'title', 'short_content', 'status', 'created_at', 'published_date')
    search_fields = ('title', 'content', 'status')
    list_filter = ('status', 'created_at', 'published_date')
    ordering = ('-created_at',)
    readonly_fields = ('file_link', 'created_at', 'published_date')

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'content', 'status')
        }),
        ('File', {
            'fields': ('file', 'file_link')
        }),
        ('Dates', {
            'fields': ('created_at', 'published_date')
        }),
    )

    def file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank">📂 Open File</a>', obj.file.url)
        return "No File"
    file_link.short_description = "File Preview"

    def short_content(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    short_content.short_description = "Content"

from django.contrib import admin
from django.utils.html import format_html
from .models import Contact, Report

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone', 'email', 'short_message', 'created_at']
    search_fields = ['name', 'subject', 'message', 'phone', 'email']
    list_filter = ['subject', 'created_at']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    short_message.short_description = 'Message'
    
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['name','email', 'address', 'screenshot_preview', 'aavedan_preview', 'document_preview']
    search_fields = ['name', 'address']
    list_filter = ['name']
    readonly_fields = ('screenshot_preview', 'aavedan_preview', 'document_preview')
    ordering = ('name',)

    fieldsets = (
        ('Basic Info', {
            'fields': ('email', 'address')
        }),
        ('Attachments', {
            'fields': ('screenshot', 'screenshot_preview', 'aavedan', 'aavedan_preview', 'document', 'document_preview')
        }),
    )

    def screenshot_preview(self, obj):
        if obj.screenshot:
            return format_html('<img src="{}" style="max-height:100px; max-width:150px;" />', obj.screenshot.url)
        return "No Screenshot"
    screenshot_preview.short_description = "Screenshot Preview"

    def aavedan_preview(self, obj):
        if obj.aavedan:
            return format_html('<img src="{}" style="max-height:100px; max-width:150px;" />', obj.aavedan.url)
        return "No Aavedan"
    aavedan_preview.short_description = "Aavedan Preview"

    def document_preview(self, obj):
        if obj.document and obj.document.url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            return format_html('<img src="{}" style="max-height:100px; max-width:150px;" />', obj.document.url)
        elif obj.document:
            return format_html('<a href="{}" target="_blank">View Document</a>', obj.document.url)
        return "No Document"
    document_preview.short_description = "Document Preview"

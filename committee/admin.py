from django.contrib import admin
from .models import Member, Position

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'member_type', 'position', 'contact_number', 'joined_date']
    list_filter = ['member_type', 'position']
    search_fields = ['name', 'email', 'quotation']
    readonly_fields = ['joined_date']
    ordering = ['-joined_date']

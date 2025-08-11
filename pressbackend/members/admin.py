from django.contrib import admin
from .models import Member
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['profile_picture','name','bio','role','contact_number','joined_date']
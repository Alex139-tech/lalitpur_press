from django.contrib import admin
from .models import Contacts,Report
# Register your models here.

@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','subject','message','phone','email']


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display =  ['name','subject','message','phone','email','address','screenshot','aavedan','document']
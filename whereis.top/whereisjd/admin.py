from django.contrib import admin
from whereisjd.models import *


class JD_Whereis_LogAdmin(admin.ModelAdmin):
    list_display = ("pk",'ip','request',"response","header",)

admin.site.register(JD_Whereis_Log,JD_Whereis_LogAdmin)
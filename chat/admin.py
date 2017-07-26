from django.contrib import admin


# Register your models here.

from django.contrib import admin
from .models import UserMessageInfo

class UserMessageInfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserMessageInfo,UserMessageInfoAdmin)

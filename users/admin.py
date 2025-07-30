from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ExceptionError

admin.site.register(CustomUser, UserAdmin)
admin.site.register(ExceptionError)
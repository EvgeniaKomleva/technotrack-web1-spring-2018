from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as OldUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(OldUserAdmin):
    pass

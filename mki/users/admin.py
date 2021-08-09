from django.contrib import admin
from django.contrib.auth.models import User, UserManager
from django.db import models
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = (
    #     "language",
    #     "currency",
    #     "superhost",
    # )

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

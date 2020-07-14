from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# decorator 방식
# admin 패널에서 User를 보고싶다, User를 컨트롤할 클래스가 아래의 클래스다.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Adimin """

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


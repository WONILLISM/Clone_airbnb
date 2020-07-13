from django.contrib import admin
from . import models

# decorator 방식
# admin 패널에서 User를 보고싶다, User를 컨트롤할 클래스가 아래의 클래스다.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Adimin """

    list_display = (
        "username",
        "email",
        "gender",
        "currency",
        "language",
        "superhost",
    )
    list_filter = (
        "language",
        "superhost",
        "currency",
    )


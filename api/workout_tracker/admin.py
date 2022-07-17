from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "first_name",
        "last_name",
        "email",
        "password",
        "sex"
    )

admin.site.register(User, UserAdmin)

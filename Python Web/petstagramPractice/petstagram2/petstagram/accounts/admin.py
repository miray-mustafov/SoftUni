from django.contrib import admin
from django.contrib.auth import get_user_model, admin as auth_admin


UserModel = get_user_model()
@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ['pk','username', 'email', 'first_name', 'last_name', 'is_staff']
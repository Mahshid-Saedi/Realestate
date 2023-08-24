from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from .models import User



class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'full_name', 'password')}),
        # ابتدا یک عنوان می گیرد بعد یک دیکشنری از فیلد ها که کلیدش را fields میگذاریم
        ('permission',
         {'fields': ('is_active', 'is_admin', 'is_superuser', 'last_login', 'groups', 'user_permissions')}),
    )

    # چون دو تا فرم داشتیم برای اون یکی داخل add_fieldsets مینویسیم
    add_fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'full_name', 'password1', 'password2')}),
    )

    search_fields = ('email', 'full_name')
    ordering = ('full_name',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)




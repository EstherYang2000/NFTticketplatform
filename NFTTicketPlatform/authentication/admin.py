from django.contrib import admin
from authentication.models import CompanyProfile,CustomerProfile,Tag,Events

admin.site.register(CompanyProfile)
admin.site.register(CustomerProfile)
admin.site.register(Tag)
admin.site.register(Events)








# admin.site.register(MyUser)
#Register your model
# class CustomUserAdmin(UserAdmin):
#     add_form = UserCreationForm
#     form = UserChangeForm
#     model = CustomUser
#     list_displlay ={'pk','email','username','firstname','lastname'}
#     add_fieldsets = UserAdmin.add_fieldsets +(
#         (None,{'fields':('email','firstname','last_name')}),
#     )
#     fieldsets = UserAdmin.fieldsets








# # from authentication.models import MyCustomer
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib import admin
#  as BaseUserAdmin

# from .models import Account
# from .form import UserCreationForm, UserChangeForm


# class AccountAdmin(BaseUserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm

#     list_display = ('email', 'name', 'walletid', 'is_staff',  'is_superuser')
#     list_filter = ('is_superuser',)

#     fieldsets = (
#         (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
#         ('Personal info', {'fields': ('name', 'walletid')}),
#         ('Groups', {'fields': ('groups',)}),
#         ('Permissions', {'fields': ('user_permissions',)}),
#     )
#     add_fieldsets = (
#         (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
#         ('Personal info', {'fields': ('name', 'walletid')}),
#         ('Groups', {'fields': ('groups',)}),
#         ('Permissions', {'fields': ('user_permissions',)}),
#     )

#     search_fields = ('email', 'name', 'walletid')
#     ordering = ('email',)
#     filter_horizontal = ()


# admin.site.register(Account, AccountAdmin)

# class MyUserAdmin(BaseUserAdmin):
#     list_display=('personal_email','personal_userName','personal_walletId','date_joined','last_login','is_admin','is_active',)
#     search_fields=('personal_email','personal_userName',)
#     readonly_fields =('date_joined','last_login')
#     filter_horizontal = ()
#     list_filter=('last_login',)
#     fieldsets = ()

#     ordering=('personal_email',)
#     add_fieldsets = (
#         (None,{
#             'classes':('wide'),
#             'fields':('personal_email','personal_userName','personal_walletId','date_joined','last_login','is_admin','is_active')
#         })
#     )

# admin.site.register(MyCustomer,MyUserAdmin)

# Register your models here.

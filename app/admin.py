from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Category,Account,Product
# Register your models here.

# admin.site.register(Category)
# admin.site.register(Account)
# class AccountAdmin(UserAdmin):
#     list_display=('email','first_name','last_name','username','last_login','date_joined','is_active')
#     list_display_links=('email','first_name','last_name')
#     readonly_fields=('last_login','date_joined')
#     ordering=('date_joined',)
#     filter_horizontal=()
#     list_filter=()
#     fieldsets=()
# admin.site.register(Account,AccountAdmin)
@admin.register(Category)
class Category(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=('category_name','slug')
    
@admin.register(Account)
class Account(admin.ModelAdmin):
    include="__all__"
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('productname',)}
    list_dispalay=('productname','price','stock','modified_date','is_available')
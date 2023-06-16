from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Order, OrderItem

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'birthday', 'street', 'house_number', 'town', 'city', 'is_staff', 'is_active')
    list_editable = ('first_name', 'last_name', 'email', 'birthday', 'street', 'house_number', 'town', 'city', 'is_staff', 'is_active')
    list_display_links = ('username',)  # 將 'username' 欄位作為連結
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

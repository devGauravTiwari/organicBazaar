from django.contrib import admin
from .models import *


class ProductImageInline(admin.StackedInline):
    model = ProductImages
    max_num = 10
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['country']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','decription','price']
    list_editable = ['price']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug':('name','decription')}

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ['basic_detail']


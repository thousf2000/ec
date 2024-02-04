from django.contrib import admin
from .models import Product, Category

class CetagoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CetagoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock','available']
    prepopulated_fields = {'slug': ('name',)}  # Add a comma after 'name'
    list_per_page = 20

admin.site.register(Product, ProductAdmin)
from django.contrib import admin

# Register your models here.

from .models import Category, Products

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['category', 'created_by', 'title', 'manufacturer', 'description', 'image', 'slug', 'price',
                    'in_stock', 'is_active', 'created', 'updated']
    list_filter = ["in_stock", 'is_active']
    list_editable = ['price', 'in_stock']

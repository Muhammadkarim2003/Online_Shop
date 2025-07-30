from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description', 'image')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

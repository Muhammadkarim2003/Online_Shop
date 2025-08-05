from django.contrib import admin
from .models import Product, Category, Order_item, Order

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
admin.site.register(Order)
admin.site.register(Order_item)

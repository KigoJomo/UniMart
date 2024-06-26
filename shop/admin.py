from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category_name", "price",)

    def category_name(self, obj):
        return obj.category.name


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

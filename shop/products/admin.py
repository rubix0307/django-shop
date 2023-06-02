from django import forms
from django.contrib import admin
from products.models import Category, CategorySub, Product, ProductSize, Size

from .models import Product


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CategorySub)
admin.site.register(Size)
admin.site.register(ProductSize)


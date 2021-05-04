from django.contrib import admin
from .models import Product, Category, Member

admin.site.register(Category)
admin.site.register(Member)
admin.site.register(Product)
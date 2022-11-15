from django.contrib import admin
from .models import Category
# Register your models here.
# class Category_admin(admin.ModelAdmin):
#     list_display=['name']
admin.site.register(Category)
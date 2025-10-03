from django.contrib import admin

from .models import Category, User

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category")


admin.site.register(Category)
admin.site.register(User)
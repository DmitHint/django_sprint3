from django.contrib import admin
from .models import Post, Category, Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text', 'pub_date',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.empty_value_display = 'Не задано'

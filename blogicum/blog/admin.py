from django.contrib import admin

from .models import Post, Category, Location


class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text', 'pub_date',)


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description',)


class LocationAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.empty_value_display = 'Не задано'
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)

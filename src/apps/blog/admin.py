from django.contrib import admin
from .models import Blog, Category, BlogView



class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'views')
    list_filter = ('title', 'category')
    search_fields = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)
    search_fields = ('title',)


class BlogViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'blog_view', 'device_id',)
    list_filter = ('blog_view', 'user', 'device_id')
    search_fields = ('blog_view', 'user', 'device_id')


admin.site.register(Blog, BlogAdmin),
admin.site.register(Category, CategoryAdmin),
admin.site.register(BlogView, BlogViewAdmin)

from django.contrib import admin
from blog.models import BlogType, Blog


# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_time', 'last_updated_time', 'author', 'blog_type')





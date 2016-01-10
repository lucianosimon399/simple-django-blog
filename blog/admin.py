from django.contrib import admin
from blog.models import Post, Category

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Post)
admin.site.register(Category)

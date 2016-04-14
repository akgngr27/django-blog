from django.contrib import admin
from blog.models import Category, Post, etiket

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("baslik",)}

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(etiket)
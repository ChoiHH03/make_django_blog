from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.
admin.site.register(Post)

#name 필드를 이용해 slug를 자동으로 채워주는 코드
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
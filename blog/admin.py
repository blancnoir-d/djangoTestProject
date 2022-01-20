from django.contrib import admin

# Register your models here.
from .models import Alert_history, Category, Tag

admin.site.register(Alert_history)


# name필드 값으로 slug 를 자동생성하도록 설정
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)

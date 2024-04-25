from django.contrib import admin
from .models import Category
from users  .models import Advertisement

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'created', 'updated','image']
    list_filter = ['created', 'updated']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('title',)}


from django.contrib import admin

from .models import Categories, News


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_filter = ('categories', 'sub_categories', 'pub_date')

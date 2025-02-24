from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContaticAdmin(admin.ModelAdmin):
    
    list_display = ('id','first_name', 'last_name', 'phone', "show")
    ordering = ('-id',)
    search_fields = ('id', 'first_name', 'last_name')
    list_per_page = 10
    list_max_show_all = 200
    list_editable = ("phone", "show")
    list_display_links = ('id', 'first_name')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_editable = ('name',)

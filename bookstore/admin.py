from django.contrib import admin
from .models import BookStore


class BookStoreAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'availability')
    list_display = ('title', 'description', 'availability')
    list_filter = ('title', 'description','availability')
    list_editable=('description', 'availability')


admin.site.register(BookStore, BookStoreAdmin)

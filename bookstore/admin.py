from django.contrib import admin
from .models import BookStore, NewsLetter


class BookStoreAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'availability')
    list_display = ('title', 'description', 'availability')
    list_filter = ('title', 'description','availability')
    list_editable=('description', 'availability')


class NewsLetterAdmin(admin.ModelAdmin):
    fields = ('title', 'description',)
    list_display = ('title', 'description')
    list_filter = ('title', 'description')
    list_editable=('description',)


admin.site.register(BookStore, BookStoreAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)
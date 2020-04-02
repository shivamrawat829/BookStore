from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'subscribed')
    list_display = ('user', 'subscribed')
    list_filter = ('user', 'subscribed')
    list_editable=('subscribed',)


admin.site.register(Profile, ProfileAdmin)
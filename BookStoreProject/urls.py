
from django.contrib import admin
from django.urls import path, include
from BookStoreProject.views import home, send_push
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('authentication.urls')),
    # path('push/', include('push_notifications.urls')),
    path('', home),
    path('send_push', send_push),
    path('webpush/', include('webpush.urls')),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript'))
]

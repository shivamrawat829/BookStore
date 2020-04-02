from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from bookstore.views import IndexView

app_name = 'bookstore'
urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('index', IndexView.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

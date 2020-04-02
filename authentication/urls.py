from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import LoginView, SignUpView, IndexView, LogoutView, subscription
app_name = 'authentication'
urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('index', IndexView.as_view(), name='index'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('subscription', subscription, name='subscription'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

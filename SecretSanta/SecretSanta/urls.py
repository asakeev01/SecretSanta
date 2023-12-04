from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from SecretSanta import settings
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('signup', views.signup),
    path('login', views.login),
    path('test_token', views.test_token),
    path("users/", include("users.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

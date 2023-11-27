from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('signup', views.signup),
    path('login', views.login),
    path('test_token', views.test_token),
    path("users/", include("users.urls")),
]

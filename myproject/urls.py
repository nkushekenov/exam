from django import views
from django.urls import path, include

from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('museum.urls')),
    path('admin/', admin.site.urls),
]

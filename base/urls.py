from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('museum.urls')),
    path('shop/', include('shop.urls')),
    path('admin/', admin.site.urls),
]

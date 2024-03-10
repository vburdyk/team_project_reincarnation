from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'museum'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('password_forgotten/', views.password_forgotten, name='password_forgotten'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

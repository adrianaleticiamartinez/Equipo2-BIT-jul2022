
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.data_view, name='data'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    # path('usuarios/register', views.register_view, name='register'),
    path('admin/', admin.site.urls),
]

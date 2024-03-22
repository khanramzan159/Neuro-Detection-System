from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('admin/', views.admin, name='admin'),
    path('main_admin/', admin.site.urls),
    path('project_running/<user_id>/', views.project, name='project')
]
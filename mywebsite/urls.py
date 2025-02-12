"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from django.http import HttpResponse
def create_admin_user(request):
    if not User.objects.filter(username="seyhan").exists():
        User.objects.create_superuser("seyhan", "bengiilhan@hotmail.com", "bengi123")
        return HttpResponse("Admin user created successfully!")
    else:
        return HttpResponse("Admin user already exists.")
def list_admin_users(request):
    users = User.objects.filter(is_superuser=True)
    if users.exists():
        return HttpResponse(", ".join([user.username for user in users]))
    return HttpResponse("No admin users found!")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('resume.urls')),
    path("create-admin/", create_admin_user),
    path("list-admins/", list_admin_users),
]



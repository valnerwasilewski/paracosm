"""
URL configuration for proj_paracosm project.

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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from app_signup.views import home, signup_view, signin_view, userslist_view, register_user



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), #página inicial
    path('signup/', signup_view, name='sign_up'),
    path('register/', register_user, name='register_user'),
    path('signin/', signin_view, name='sign_in'),
    path('users/', userslist_view, name="users_list")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
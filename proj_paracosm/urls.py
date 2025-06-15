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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app_signup.views import (home, register_user, registration_completed_view,
                              signin_view, signup_view, userslist_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page
    path('signup/', signup_view, name='sign_up'),
    path('register/', register_user, name='register_user'),
    path('signin/', signin_view, name='sign_in'),
    path('users/', userslist_view, name="users_list"),
    path(
        'registration/',
        registration_completed_view,
        name="registration_completed"
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

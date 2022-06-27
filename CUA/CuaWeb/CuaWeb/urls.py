"""CuaWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import RedirectView
from django.conf.urls import url
from django.urls import path, include
from httplib2 import RedirectLimit
from CuaApp import views
from django.contrib.auth import views as auth_views
#
# from CuaWeb import CuaApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),    
]
urlpatterns += [
    url(r'^CuaApp/', include('CuaApp.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    
]
urlpatterns += [
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
"""backend URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from login import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('timecheck/', include('timecheck.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('token/', obtain_auth_token, name='token'),
    path('blog/api/',include('blog.urls')),
]

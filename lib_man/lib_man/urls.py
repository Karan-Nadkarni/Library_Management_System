"""lib_man URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name="home"),
    path('bi/',views.bi,name="bi"),
    path('br/',views.br,name="br"),
    path('sr/',views.sr,name="sr"),
    path('reg/',views.reg,name="reg"),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name="signout"),
    path('reg/regsub',views.regsub,name='regsub'),
    path('signin/login_sub',views.login_sub,name='login_sub'),
    path('signout/logout_sub',views.logout_sub,name='logout_sub'),
    path('bi/bi_sub',views.bi_sub,name='bi_sub'),
    path('br/br_sub',views.br_sub,name='br_sub'),
]

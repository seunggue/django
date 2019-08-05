"""django_intro URL Configuration

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
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('greeting/<str:name>/',views.greeting),
    path('cube/<int:num>/', views.cube),
    path('mul/<int:num1>/<int:num2>/', views.mul),
    path('dtl/', views.dtl),
    path('christmas/', views.christmas),
]
# 'dinner라는 경로가 들어오면 views의 dinner를 실행시켜줘
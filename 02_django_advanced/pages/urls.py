from django.urls import path
from . import views 

urlpatterns = [
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('post-ping/', views.post_ping),
    path('post-pong/', views.post_pong),
    path('static-example/', views.static_example),
]

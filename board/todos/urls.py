from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),

    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    path('add/', views.add, name='add'),

    path('<int:id>/update/', views.update, name='update'),

    path('<int:id>/delete/', views.delete, name='delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    # create
    path('new/', views.new),
    path('create/', views.create),

    #read
    path('', views.index),

    path('<int:question_id>/answer/create/', views.answer_create),
]

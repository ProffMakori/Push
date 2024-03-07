
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('post_detail/', views.post_detail, name='post_detail'),

]

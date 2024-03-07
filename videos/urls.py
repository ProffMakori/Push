from django.contrib import admin
from django.urls import path
from videos import views

urlpatterns = [
    path('videos/', views.video_list, name='video_list'),
    path('videos/<int:video_id>/', views.video_detail, name='video_detail'),


]

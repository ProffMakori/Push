
from django.contrib import admin
from django.urls import path
from notifications import views

urlpatterns = [
    path('notifications/', views.notifications, name='signup'),

]

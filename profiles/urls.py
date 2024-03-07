from django.contrib import admin
from django.urls import path
from profiles import views

urlpatterns = [
    path('profile/', views.profile, name='login'),

]

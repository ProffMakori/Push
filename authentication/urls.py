
from django.contrib import admin
from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('add_personal_info/', views.add_personal_info, name='add_personal_info'),

]

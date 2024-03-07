
from django.contrib import admin
from django.urls import path
from meet_your_crush import views

urlpatterns = [
    path('meet_your_crush', views.meet_your_crush, name='meet_your_crush'),
]

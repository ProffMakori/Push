
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('posts.urls')),
    path('', include('messaging.urls')),
    path('', include('videos.urls')),
    path('', include('notifications.urls')),
    path('', include('meet_your_crush.urls')),
    path('', include('profiles.urls')),
]

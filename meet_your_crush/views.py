# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Crush


def meet_your_crush(request):
    crushes = Crush.objects.filter(online=True).exclude(user=request.user)
    return render(request, 'meet_your_crush/meet_your_crush.html', {'crushes': crushes})

# Add more views for connecting, rating, etc.

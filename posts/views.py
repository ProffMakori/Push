# Create your views here.
from django.shortcuts import render, redirect
from .models import Post


def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(author=request.user, content=content)
            return redirect('home')  # Assuming 'home' is the homepage URL name
    return render(request, 'posts/create_post.html')


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

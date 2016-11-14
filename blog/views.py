from django.shortcuts import render
from blog.models import posts
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")

def home(request):
    entries = posts.objects.all()[:10]
    return render(request, 'blog.html', {'posts' : entries})
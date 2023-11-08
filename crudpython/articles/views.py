from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def article_data(request):
    articles= Article.objects.all().orderby('date')
    return render(request,'articles/article_data.html',{'articles':articles})

def article_about(request):
    return render(request, 'articles/article_about.html')

def article_detail(request, slug):
    return HttpResponse(slug)
# Create your views here.

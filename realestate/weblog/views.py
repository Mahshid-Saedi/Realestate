from django.shortcuts import render
from django.views import View
from .models import BlogModel

class BlogView(View):
    def get(self, request):
        blogs = BlogModel.objects.all()
        return render(request, 'weblog/blog.html', {'blogs':blogs})


class DetailBlogView(View,):
    def get(self, request):
        return render(request, 'weblog/single_blog.html')
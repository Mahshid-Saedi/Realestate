from django.urls import path
from . import views

app_name = 'weblog'

urlpatterns = [
   path('blogs', views.BlogView.as_view(), name = 'blog' ),
   path('blogs/<int:slug>/', views.DetailBlogView.as_view(), name = 'single_blog'),

]
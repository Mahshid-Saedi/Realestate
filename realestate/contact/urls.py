from django.urls import path
from . import views

app_name='contact'
urlpatterns = [
    path('allpost', views.ContactView.as_view(), name = 'posts'),
    path('post/<int:post_id>/<slug:post_slug>/', views.PostDetailView.as_view(), name = 'post_detail'),
    path('post/create/', views.PostView.as_view(), name = 'post_create'),
    path('reply/<int:post_id>/<int:comment_id>/', views.PostAddReplyView.as_view(), name = 'add_reply'),

]
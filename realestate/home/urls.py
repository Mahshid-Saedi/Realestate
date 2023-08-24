from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
       path('', views.HomeView.as_view(), name = 'home'),
       path('category/' ,views.HomeView.as_view(), name = 'category_filter'),
       path('<slug:slug>/' ,views.RealestateDetailView.as_view(), name = 'realestate_detail'),

]
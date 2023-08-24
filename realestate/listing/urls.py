from django.urls import path
from . import views
app_name = 'listing'

urlpatterns = [
    path('listings', views.ListingView.as_view(), name = 'real_list'),
    path('orders/', views.SearchView.as_view(), name = 'order'),
]
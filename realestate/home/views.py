from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import RealEstateModel,CategoryModel


class HomeView(View):

    def get(self, request):
        realestates = RealEstateModel.objects.order_by('-id')[:4]
        salerealestate = RealEstateModel.objects.filter(type_category__transaction='فروش').order_by('-id')[:2]
        rentrealestate = RealEstateModel.objects.filter(type_category__transaction='اجاره').order_by('-id')[:2]
        return render(request, 'home/home.html',{'realestates':realestates, 'salerealestate':salerealestate,'rentrealestate':rentrealestate})

class RealestateDetailView(View):
    def get(self, request, slug):
        realdetail = get_object_or_404(RealEstateModel, slug = slug)
        return render(request, 'home/detail.html', {'realdetail':realdetail})











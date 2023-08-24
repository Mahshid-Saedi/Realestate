from django.shortcuts import render,get_object_or_404
from django.views import View
from home.models import RealEstateModel


class ListingView(View):
    def get(self, request):
        realestates = RealEstateModel.objects.all()
        return render(request, 'listing/order.html', {'realestates':realestates})




class SearchView(View):
    def get(self, request):
        realestates = RealEstateModel.objects.all()
        if 'bedroom' in request.GET :
            bedroom = request.GET['bedroom']
            realestates = realestates.filter(bedroom=bedroom)

        return render(request, 'listing/order.html', {'realestates':realestates})






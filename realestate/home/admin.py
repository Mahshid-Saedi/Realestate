from django.contrib import admin
from .models import RealEstateModel, CategoryModel

admin.site.register(CategoryModel)
@admin.register(RealEstateModel)
class RealEstateAdmin(admin.ModelAdmin):
    raw_id_fields = ('type_category',)

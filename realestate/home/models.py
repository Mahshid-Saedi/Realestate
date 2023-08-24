from django.db import models
from django.urls import reverse


class CategoryModel(models.Model):
    transaction_type = (
        ('فروش','فروش'),
        ('اجاره','اجاره'),
    )
    transaction = models.CharField(max_length=20, choices=transaction_type, default='فروش')
    property_type = (
        ('مسکونی','مسکونی'),
        ('ویلایی','ویلایی'),
        ('آپارتمان','آپارتمان'),
        ('خانه های تک خانوار','خانه های تک خانوار'),
        ('دفاتر','دفاتر'),
        ('زمین','زمین'),
        ('زمین کشاورزی','زمین کشاورزی'),
        ('باغ','باغ'),
    )
    propertytype = models.CharField(max_length=100, choices=property_type, default='مسکونی')


    class Meta:
        ordering = ('propertytype',)

    def __str__(self):
        return self.propertytype

    def get_absolute_url(self):
        return reverse('home:category_filter')




class RealEstateModel(models.Model):
    type_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='realestate')
    name = models.CharField(max_length=100, blank=True)
    price = models.IntegerField()
    meterage = models.IntegerField()
    address = models.TextField()
    bathroom_and_toilet = models.IntegerField(blank=True)
    bedroom = models.IntegerField(blank=True)
    year_of_construction = models.CharField(max_length=100, null=True, blank=True)
    detail = models.TextField()
    descriptions = models.TextField()
    main_image = models.ImageField(upload_to='real_estates/%Y/%m/%d/')
    image1 = models.ImageField(upload_to='real_estates/%Y/%m/%d/')
    image2 = models.ImageField(upload_to='real_estates/%Y/%m/%d/')
    image3 = models.ImageField(upload_to='real_estates/%Y/%m/%d/')
    slug = models.SlugField(max_length=100, unique=True)
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True,blank=True, null=True)
    updated = models.DateField(auto_now=True,blank=True, null=True)


    class Meta:
        ordering = ('type_category',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:realestate_detail', args=[self.slug,])

    def split(self):
        return self.detail.split('\n')

    def lasts(self):
        return RealEstateModel.objects.last()










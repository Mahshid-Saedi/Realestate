from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls', namespace = 'home')),
    path('account/', include('account.urls', namespace = 'account')),
    path('listing/', include('listing.urls', namespace = 'listing')),
    path('contact/', include('contact.urls', namespace = 'contact')),
    path('weblog/', include('weblog.urls', namespace = 'weblog')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

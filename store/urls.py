from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from store.views import *

urlpatterns = [
    path('', home, name = 'name'),
    path('contact', contact, name = 'contact'),
    path('products/<slug>/', products, name = 'products'),
    path('register', register, name = 'register'),
    path('single', single, name = 'single'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

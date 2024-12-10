from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from store.views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('product/<slug>', products, name = 'products'),
    path('single/<int:pk>/', single, name = 'single'),
]

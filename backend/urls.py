from django.urls import path
from .views import *

urlpatterns = [
    path('fast_food/', fast_food),
    path('pizza/', pizza),
    path('coffee/', coffee),
    path('drink/', drink),
    path('help/', help),
    path('order/', order),
    
]

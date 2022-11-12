from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('fast_food/', fast_food),
    path('pizza/', pizza),
    path('coffee/', coffee),
    path('drink/', drink),
    path('help/', help),
    path('order/', order),
]

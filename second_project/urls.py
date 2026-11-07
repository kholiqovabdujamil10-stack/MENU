from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('menu/', menu),
    path('popular/', popular),
    path('about/', about),
    path('contact/', contact),
]
from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('about', about),
    path('contact', contact),
    path('product', product),
    path('remot', remot),
    path('video', video),
    path('product_detail/<int:id>', product_detail)
]
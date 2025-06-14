
from django.urls import path
from .views import *

urlpatterns = [
    path('products/', product_list),
    path('products/show_products/', show_products ,name='show_products')

]
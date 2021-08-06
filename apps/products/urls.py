from django.urls import path, include
from .views import *

app_name = 'products'

urlpatterns = [
    path('categories/', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),

    path('products/', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),

]

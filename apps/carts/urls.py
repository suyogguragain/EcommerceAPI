from django.urls import path, include
from .views import *

app_name = 'products'

urlpatterns = [
    path('', ListCart.as_view(), name='allcarts'),
    path('<int:pk>/', DetailCart.as_view(), name='cartdetail'),

]

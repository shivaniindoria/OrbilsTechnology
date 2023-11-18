from django.urls import path
from orbils.cart_view import *
from orbils.api_view import *

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('cart/create/', CartView.as_view()),
    path('cart/delete/', CartView.as_view()),
    path('fun-fact/', FunFactAPIView.as_view()),
    path('quote/', RandomQuoteAPIView.as_view()),
]
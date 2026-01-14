from django.urls import path
from .views import CartView, AddToCartView, UpdateCartItemView, RemoveCartItemView

urlpatterns = [
    path('', CartView.as_view(), name='view_cart'),
    path('add/', AddToCartView.as_view(), name='add_to_cart'),
    path('update/', UpdateCartItemView.as_view(), name='update_cart_item'),
    path('remove/', RemoveCartItemView.as_view(), name='remove_cart_item'),
]
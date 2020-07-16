from django.urls import path
from .import views as store_views

urlpatterns = [
    path('', store_views.store, name='store'),
    path('cart/', store_views.cart, name='cart'),
    path('checkout/', store_views.checkout, name='checkout'),
    path('update_item/', store_views.updateItem, name='update_item'),
    path('process_order/', store_views.processOrder, name='process_order'),
]

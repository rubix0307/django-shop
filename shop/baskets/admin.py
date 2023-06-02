from django.contrib import admin
from baskets.models import Basket, BasketItem, Order, OrderItem

admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(Order)
admin.site.register(OrderItem)

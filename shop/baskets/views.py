from baskets.models import Basket, BasketItem
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, render
from products.models import Category, CategorySub, Product, ProductSize, Size


def basket_view(request):
    user = request.user

    basket, created = Basket.objects.get_or_create(user=user)

    # получаем все элементы корзины пользователя
    basket_items = basket.basketitem_set.all()

    context = {
        'title': 'Твоя корзина',
        'categories': Category.objects.all(),
        'basket': basket,
        'basket_items': basket_items,
    }
    for item in basket_items:
        pass
    return render(request, r'baskets\basket.html', context=context)


def basket_update(request: WSGIRequest, action: str, product_id: int):
    user = request.user

    size = request.GET.get('size', None)
    
    product = Product.objects.get(id=product_id)
    size = Size.objects.get(name=size)
    product_size = ProductSize.objects.get(product=product, size=size)

    basket, created = Basket.objects.get_or_create(user=user)
    basket_item, created = BasketItem.objects.get_or_create(basket=basket, product_size=product_size, defaults={'quantity': 0})
    
    if action == 'add':
        basket_item.quantity += 1
        if basket_item.product_size.quantity < basket_item.quantity:
            basket_item.quantity = basket_item.product_size.quantity

    elif action == 'remove':
        if basket_item.quantity > 0:
            basket_item.quantity -= 1

    if basket_item.quantity > 0:
        basket_item.save()
    else:
        basket_item.delete()

    product_sizes = ProductSize.objects.filter(product=product)

    context = {
        'categories': Category.objects.all(),
        'product': product,
        'product_sizes': product_sizes,

        'basket_item': basket_item,
    }

    return render(request, 'products\product.html', context=context)
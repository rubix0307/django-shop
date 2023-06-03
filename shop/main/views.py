from django.core.handlers.wsgi import WSGIRequest
from products.models import Category, Product, ProductSize, Size


def home(request: WSGIRequest):
    user = request.user

    # product = Product.objects.get(name='Платье1')
    # size = Size.objects.get(name='M')
    # product_size = ProductSize.objects.get(product=product, size=size)

    # basket, created = Basket.objects.get_or_create(user=user)
    # basket_item, created = BasketItem.objects.get_or_create(basket=basket, product_size=product_size, defaults={'quantity': 0})
    # basket_item.quantity += 1
    # basket_item.save()

    # basket_items = BasketItem.objects.filter(basket=basket)

    products = Product.objects.all()
    products_sizes = {product.id: ProductSize.objects.filter(product=product) for product in products}
    context = {
        'title': 'Главная страница',
        # 'basket': basket_items,
        'categories': Category.objects.all(),
        'products': products,
        'products_sizes': products_sizes,
    }

    return render(request, 'main\home.html', context=context)






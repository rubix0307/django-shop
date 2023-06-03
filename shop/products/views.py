from baskets.models import Basket, BasketItem
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, render
from products.models import Category, CategorySub, Product, ProductSize, Size


def category_view(request: WSGIRequest, category_slug, subcategory_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = None
    
    if subcategory_slug:
        subcategory = get_object_or_404(CategorySub, slug=subcategory_slug, category=category)
        products = Product.objects.filter(subcategory=subcategory)
    else:
        products = Product.objects.filter(category=category)
    
    # Получение доступных размеров для каждого товара
    products_sizes = {product.id: ProductSize.objects.filter(product=product) for product in products}

    context = {
        'title': category.name,
        'categories': Category.objects.all(),
        'category': category,
        'subcategory': subcategory,
        'products': products,
        'products_sizes': products_sizes, 
    }
    for product in products:
        pass

    return render(request, 'main/home.html', context=context)



def product_view(request: WSGIRequest, product_slug:str):

    product = Product.objects.get(slug=product_slug)
    product_sizes = ProductSize.objects.filter(product=product)

    context = {
        'title': product.name,
        'categories': Category.objects.all(),
        'product': product,
        'product_sizes': product_sizes,
    }

    return render(request, 'products\product.html', context=context)








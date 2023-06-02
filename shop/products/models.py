from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from transliterate import translit
# Create your models here.

def custom_slugify(value):
    slug = slugify(value, allow_unicode=True)
    slug = translit(slug, 'ru', reversed=True)
    return slug


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(max_length=200, unique=True, populate_from='name', slugify=custom_slugify)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CategorySub(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = AutoSlugField(max_length=200, unique=True, populate_from='name', slugify=custom_slugify)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_sub_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(max_length=200, unique=True, populate_from='name', slugify=custom_slugify)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(CategorySub, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Size(models.Model):
    name = models.CharField(max_length=5)  # For 'XS', 'S', 'M', 'L', 'XL', '30', '31', '32' etc.

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

class ProductSize(models.Model):
    product = models.ForeignKey(Product, related_name='sizes', on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name[:10]} - {self.size.name}"

    class Meta:
        verbose_name = 'Размер товара'
        verbose_name_plural = 'Размеры товаров'
        ordering = ['size__id']
    
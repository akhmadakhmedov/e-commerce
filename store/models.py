from django.urls.base import reverse
from category.models import Category
from django.db import models

class Cover(models.Model):
    cover_title         = models.CharField(max_length=20, blank=True)
    cover_description   = models.CharField(max_length=30, blank=True)
    cover_image         = models.ImageField(upload_to='photos/covers')

    def __str__(self):
        return self.cover_title

class Product(models.Model):
    product_name        = models.CharField(max_length=50, unique=True)
    slug                = models.SlugField(max_length=50, unique=True)
    description         = models.TextField(max_length=500, blank=True)
    old_price           = models.IntegerField()
    price               = models.IntegerField()
    images              = models.ImageField(upload_to='photos/products')
    stock               = models.IntegerField()
    is_available        = models.BooleanField(default=True)
    is_popular          = models.BooleanField(default=False)
    is_newarrived       = models.BooleanField(default=False)
    is_recommended      = models.BooleanField(default=False)
    category            = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date        = models.DateTimeField(auto_now_add=True)
    modified_date       = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

    
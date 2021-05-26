from django.shortcuts import render, get_object_or_404
from store.models import Product, Cover
from category.models import Category

def home(request):
    products_popular     = Product.objects.all().filter(is_popular=True)
    products_newarrived  = Product.objects.all().filter(is_newarrived = True)
    products_recommended = Product.objects.all().filter(is_recommended = True)
    covers               = Cover.objects.all()

    context = {
        'products_popular' : products_popular,
        'products_newarrived': products_newarrived,
        'products_recommended': products_recommended,
        'covers': covers,
    }
    return render(request, 'home.html', context)


def popular_store(request, category_slug = None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products_popular = Product.objects.filter(category = categories, is_available = True, is_popular=True)
        product_count = products.count()
    else:
        products_popular = Product.objects.all().filter(is_available = True, is_popular=True)
        product_count = products_popular.count()

    context = {
        'products_popular': products_popular,
        'product_count': product_count,
    }
    return render(request, 'popular_store.html', context)

def recommended_store(request, category_slug = None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products_recommended = Product.objects.filter(category = categories, is_available = True, is_recommended=True)
        product_count = products.count()
    else:
        products_recommended = Product.objects.all().filter(is_available = True, is_recommended=True)
        product_count = products_recommended.count()

    context = {
        'products_recommended': products_recommended,
        'product_count': product_count,
    }
    return render(request, 'recommended_store.html', context)

def newarrived_store(request, category_slug = None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products_newarrived = Product.objects.filter(category = categories, is_available = True, is_newarrived=True)
        product_count = products.count()
    else:
        products_newarrived = Product.objects.all().filter(is_available = True, is_newarrived=True)
        product_count = products_newarrived.count()

    context = {
        'products_newarrived': products_newarrived,
        'product_count': product_count,
    }
    return render(request, 'newarrived_store.html', context)


    
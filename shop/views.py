from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Product

def shop(request):
    return render(request, 'shop/index.html')

def get_products(request, category):
    if category == "undefined":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__name=category)

    data = [{'name': product.name, 'price': product.price}
            for product in products]
    return JsonResponse(data, safe=False)


def search_products(request):
    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(Q(name__icontains=query))
        data = [{'name': product.name, 'price': product.price}
                for product in products]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse([], safe=False)

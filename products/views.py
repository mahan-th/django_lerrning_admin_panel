from django.shortcuts import render

# Create your views here.
from .models import Product


def product_list(request):
    # This view will render a list of products
    #context = {
    #    'products': Product.objects.all()
    #}
    return render(request, 'products.html')


def show_products(request):
    
    context = {
        'products': Product.objects.all()
    }
    search = request.GET.get('q')
    
    if search:
        context['products'] = Product.objects.filter(name=search)

    return render(request, 'product_list.html', context)



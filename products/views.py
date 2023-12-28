from django.shortcuts import render
from products.models import Product
from django.views.generic import DetailView

# Create your views here.


class ProductDetailView(DetailView):
    model = Product
    
    template_name = "products/productdetail.html"


def index(request):
    fashion_products = Product.objects.filter(category__name='Fashion')
    electronic_products = Product.objects.filter(category__name='Electronics')
    jewels_products = Product.objects.filter(category__name='Accessories')
    print(jewels_products)
    context = {'fashion_products1':fashion_products[:3],'fashion_products2':fashion_products[3:6]}
    context['electronic_products1']= electronic_products[:3] 
    context['electronic_products2'] = electronic_products[3:6]
    context['jewels_products1'] = jewels_products[:3]
    context['jewels_products2'] = jewels_products[3:6]

    return render(request,'products/index.html',context)

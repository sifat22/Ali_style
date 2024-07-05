from django.shortcuts import render,get_object_or_404
from.models import Product

# Create your views here.


def product_details(request, product_slug):
    try:
        product_detail = get_object_or_404(Product,slug = product_slug)

    except Exception as e:
        raise e
    return render(request,"app_product_store/product_details.html",{
        "product_detail" : product_detail,
        
    })


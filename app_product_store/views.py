from django.shortcuts import render,get_object_or_404
from.models import Product
from app_brands.models import Brand
from app_subcategory.models import Category

# Create your views here.


def store(request, brand_slug=None, category_slug=None):
    products = None
    categories = None
    brands = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug)
        brands = get_object_or_404(Brand, slug = brand_slug)
        products = Product.objects.filter(category = categories, is_available= True)
        cat_by_brand = Category.objects.filter(brand = brands)

        product_count = products.count()

    elif brand_slug !=None:
        brands = get_object_or_404(Brand, slug = brand_slug)
        products = Product.objects.filter(brand = brands, is_available= True)
        cat_by_brand = Category.objects.filter(brand = brands)
        product_count = products.count()

    # elif brand_slug and brand_slug != None:
    #     brands = get_object_or_404(Brand, slug = brand_slug)
    #     categories = get_object_or_404(Category, slug = category_slug)
    #     products = Product.objects.filter(brand = brands, category = categories, is_available= True)
    #     product_count = products.count()

    else:
        products = Product.objects.all().filter(is_available=True).order_by("-modified_date")
        cat_by_brand = Category.objects.all()[:0]
        product_count = products.count()


    return render(request,"app_product_store/store.html",{
        "products" : products,
        "product_count" : product_count,
        "cat_by_brand" : cat_by_brand

    })


def product_details(request, brand_slug, category_slug, product_slug):
    try:
        product_detail = get_object_or_404(Product, brand__slug = brand_slug, category__slug = category_slug, slug = product_slug)

    except Exception as e:
        raise e
    return render(request,"app_product_store/product_details.html",{
        "product_detail" : product_detail,
        
    })


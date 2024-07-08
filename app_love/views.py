from django.shortcuts import render,redirect,get_object_or_404
from .models import WishlistItem,Wishlist
from app_product_store.models import Product
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def _wishlist_id(request):
    wishlist = request.session.session_key
    if not wishlist:
        wishlist = request.session.create()
    return wishlist


def add_wishlist(request, product_id):
    product = Product.objects.get(id = product_id)
    wishlist_item = []
    if request.method == 'POST':
        try:
            wishlist = Wishlist.objects.get(wishlist_id = _wishlist_id(request))
        except Wishlist.DoesNotExist:
            wishlist =  Wishlist.objects.create(
                wishlist_id = _wishlist_id(request)
            )
        wishlist.save()

        if WishlistItem.objects.filter(wishlist = wishlist, product = product).exists():
            return redirect("wishlist")
        else:
            wishlist_item = WishlistItem.objects.create(
                product = product,
                wishlist = wishlist
            )
        wishlist_item.save()
    return redirect("wishlist")


def delete_wishlist(request, product_id):
    wishlist = Wishlist.objects.get(wishlist_id = _wishlist_id(request))
    product = get_object_or_404(Product, id = product_id)
    wishlist_item = WishlistItem.objects.get(product = product, wishlist=wishlist)
    wishlist_item.delete()
    return redirect("wishlist")

    


def wishlist(request):
    try:
        wishlist = Wishlist.objects.get(wishlist_id = _wishlist_id(request))
        wishlist_item = WishlistItem.objects.filter(wishlist = wishlist, is_active = True)
    except ObjectDoesNotExist:
        pass
    return render(request,"app_love/love.html",{
        "wishlist_item" : wishlist_item

    })

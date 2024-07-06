from django.urls import path
from . import views

urlpatterns = [
    path("",views.store,name="store"),
    path("<slug:brand_slug>/",views.store,name="products_by_brand"),
    path("<slug:category_slug>/",views.store,name="products_by_category"),
    path("<slug:brand_slug>/<slug:category_slug>/",views.store,name="products_by_b_c"),
    path("<slug:brand_slug>/<slug:category_slug>/<slug:product_slug>/",views.product_details,name="product_details"),
    
]

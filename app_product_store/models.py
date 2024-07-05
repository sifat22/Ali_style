from django.db import models
from app_brands.models import Brand
from app_subcategory.models import Category
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="photos/app_product",blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    stock = models.IntegerField()
    import_from = models.CharField(max_length=200)
    price = models.IntegerField()
    manufacture = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    offers = models.BooleanField(default=False)
    warrenty = models.IntegerField()
    offer_precentage = models.IntegerField()
    delivery_time = models.CharField(max_length=200,blank=True)
    img1 = models.ImageField(upload_to="photos/app_product",blank=True)
    img2 = models.ImageField(upload_to="photos/app_product",blank=True)
    img3 = models.ImageField(upload_to="photos/app_product",blank=True)
    img4 = models.ImageField(upload_to="photos/app_product",blank=True)
    desc = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('product_details', args=[self.slug])
    


    def __str__(self):
        return self.product_name
    


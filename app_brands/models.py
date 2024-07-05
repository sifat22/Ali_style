from django.db import models

# Create your models here.


class Brand(models.Model):
    brand_name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.brand_name
    


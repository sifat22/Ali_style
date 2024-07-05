# Generated by Django 3.1 on 2024-07-05 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_product_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_time', models.CharField(max_length=200)),
                ('img1', models.ImageField(blank=True, upload_to='photos/product_detail')),
                ('img2', models.ImageField(blank=True, upload_to='photos/product_detail')),
                ('img3', models.ImageField(blank=True, upload_to='photos/product_detail')),
                ('img4', models.ImageField(blank=True, upload_to='photos/product_detail')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_product_store.product')),
            ],
        ),
    ]

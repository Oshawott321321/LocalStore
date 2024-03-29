# Generated by Django 3.1.1 on 2020-12-22 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_product_quantity', models.PositiveSmallIntegerField()),
                ('cart_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.cart')),
                ('cart_product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]

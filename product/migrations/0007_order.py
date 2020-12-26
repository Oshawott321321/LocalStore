# Generated by Django 3.1.1 on 2020-12-23 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_cart_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_amount', models.PositiveIntegerField()),
                ('order_address', models.CharField(max_length=300, null=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.cart')),
            ],
        ),
    ]
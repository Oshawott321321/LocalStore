# Generated by Django 3.1.1 on 2020-12-22 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201222_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=100)),
                ('pro_price', models.FloatField()),
                ('pro_image', models.ImageField(blank=True, null=True, upload_to='product')),
                ('pro_des', models.CharField(blank=True, max_length=1000)),
                ('pro_quantity', models.PositiveIntegerField(default=0)),
                ('pro_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.shop')),
            ],
        ),
    ]

# Generated by Django 3.1.1 on 2020-12-22 06:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appuser', '0005_auto_20201221_2117'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shops',
            new_name='Shop',
        ),
    ]
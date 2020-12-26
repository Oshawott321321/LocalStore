# Generated by Django 3.1.1 on 2020-12-22 16:11

import card.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DebitCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.BigIntegerField(validators=[card.models.check_card_number, django.core.validators.MinValueValidator(4000000000000000, message='Please enter Card NUmber which is > 4000000000000000')])),
                ('card_cvv', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(100, message='Cvv must be > 100'), django.core.validators.MaxValueValidator(999, message='Cvv must be < 999')])),
                ('card_name', models.CharField(max_length=100)),
                ('card_exp_month', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(12, message='It is not Valid Month'), django.core.validators.MinValueValidator(1, message='It is not Valid Month')])),
                ('card_exp_year', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2030, message='It is not Valid Year'), django.core.validators.MinValueValidator(2020, message='It is not Valid Year')])),
                ('card_balance', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
# Create your models here.

def check_card_number(value):
        if len(str(value)) != 16:
                raise ValidationError('Card Length Must be 16')
        return

class DebitCard(models.Model):
    card_number =models.BigIntegerField(
                validators=[check_card_number,
                                validators.MinValueValidator(4000000000000000,message='Please enter Card NUmber which is > 4000000000000000')]
    )
    card_cvv = models.SmallIntegerField(
                validators=[
                        validators.MinValueValidator(100 ,message='Cvv must be > 100'),
                        validators.MaxValueValidator(999 ,message='Cvv must be < 999')
                ]
    ) # amx value and min value 
    card_name = models.CharField(max_length=100)
    card_exp_month = models.PositiveSmallIntegerField(null=True,
                    validators=[
                            validators.MaxValueValidator(12, message='It is not Valid Month'),
                            validators.MinValueValidator(1, message='It is not Valid Month')])
    card_exp_year = models.PositiveSmallIntegerField(null=True,
                    validators=[
                            validators.MaxValueValidator(2030, message='It is not Valid Year'),
                            validators.MinValueValidator(2020, message='It is not Valid Year')])
    card_balance = models.PositiveIntegerField(default=0)

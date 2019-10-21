from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Product_Name'
                            )
    price = models.IntegerField(verbose_name='Product_Price')
    description = models.TextField(verbose_name='Product_Description')
    stock = models.IntegerField(verbose_name='Product_Stock')
    register_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Date Registered'
                                         )

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'bk_product'
        verbose_name = 'BK Product'
        verbose_name_plural = 'BK Product'




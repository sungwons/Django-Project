from django.db import models

# Create your models here.

class Order(models.Model):
    # 1-N Relationship: Foreingkey('AppName.ClassName')
    bkuser = models.ForeignKey('bkuser.Bkuser',
                               on_delete=models.CASCADE,
                               verbose_name='User'
                               )
    product = models.ForeignKey('product.Product',
                               on_delete=models.CASCADE,
                               verbose_name='Product'
                               )
    quantity = models.IntegerField(verbose_name='Quantity')
    register_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Date Registerd')

    def __str__(self):
        return str(self.bkuser) + ' ' + str(self.product)


    class Meta:
        db_table = 'bk_order'
        verbose_name = 'BK Order'
        verbose_name_plural = 'BK Order'


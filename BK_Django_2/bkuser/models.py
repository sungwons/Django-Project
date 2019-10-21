from django.db import models

# Create your models here.

class Bkuser(models.Model):
    email = models.EmailField(verbose_name='Email')
    password = models.CharField(max_length=128,
                                verbose_name='Password'
                                )
    level = models.CharField(max_length=8,
                             verbose_name='Level',
                             choices=(
                                 ('admin', 'admin'),
                                 ('user', 'user')
                             ))
    register_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Date Registered'
                                         )

    def __str__(self):
        return self.email


    class Meta:
        db_table = 'bk_user'
        verbose_name = 'BK User'
        verbose_name_plural = 'BK User'




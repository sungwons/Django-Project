from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="Tag Name")
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='Time created')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brandon_tag'
        # App Name change
        verbose_name_plural = "Brandon's Tag"
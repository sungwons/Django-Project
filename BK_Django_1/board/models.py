from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='Title')
    contents = models.TextField(verbose_name='Content')
    # ForeignKey: 1-N Relationship
    writer = models.ForeignKey('bkuser.Bkuser',
                               on_delete=models.CASCADE,
                               verbose_name='Writer')
    # ManyToManyField: N-M Relationship
    tags = models.ManyToManyField('tag.Tag',
                                  verbose_name="Tag")
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='Time created')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'brandon_content'
        # App Name change
        verbose_name_plural = "Brandon's Board"
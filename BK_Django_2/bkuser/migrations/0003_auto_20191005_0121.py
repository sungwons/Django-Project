# Generated by Django 2.2.6 on 2019-10-05 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bkuser', '0002_bkuser_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bkuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='Password'),
        ),
    ]

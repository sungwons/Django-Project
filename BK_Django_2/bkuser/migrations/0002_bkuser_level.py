# Generated by Django 2.2.6 on 2019-10-04 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bkuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bkuser',
            name='level',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=8, verbose_name='Level'),
            preserve_default=False,
        ),
    ]
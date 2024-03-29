# Generated by Django 2.2.5 on 2019-09-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bkuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='User Name')),
                ('useremail', models.EmailField(max_length=128, verbose_name='User Email')),
                ('password', models.CharField(max_length=64, verbose_name='Password')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
            ],
            options={
                'verbose_name_plural': "Brandon's Users",
                'db_table': 'brandon_user',
            },
        ),
    ]

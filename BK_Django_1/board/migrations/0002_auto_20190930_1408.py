# Generated by Django 2.2.5 on 2019-09-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='Writer',
            new_name='writer',
        ),
        migrations.AddField(
            model_name='board',
            name='tags',
            field=models.ManyToManyField(to='tag.Tag', verbose_name='Tag'),
        ),
    ]

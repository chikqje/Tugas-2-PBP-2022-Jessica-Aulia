# Generated by Django 4.1 on 2022-09-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_rename_rating_mywatchlist_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='Title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mywatchlist',
            name='Watched',
            field=models.CharField(default='', max_length=255),
        ),
    ]

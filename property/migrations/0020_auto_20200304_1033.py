# Generated by Django 2.2.4 on 2020-03-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20200224_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(verbose_name='Новостройка'),
        ),
    ]

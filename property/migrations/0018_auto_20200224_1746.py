# Generated by Django 2.2.4 on 2020-02-24 14:46

from django.db import migrations


def set_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        owners_flats = Flat.objects.filter(owner=owner.name)
        owner.flats.set(owners_flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20200224_1745'),
    ]

    operations = [
        migrations.RunPython(set_flats_to_owners)
    ]

# Generated by Django 3.0.6 on 2020-05-29 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fotonovs', '0006_albumn_photon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albumn',
            options={'ordering': ('name',), 'verbose_name': 'albumn', 'verbose_name_plural': 'albumns'},
        ),
    ]
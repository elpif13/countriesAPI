# Generated by Django 5.0.6 on 2024-05-14 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0004_alter_countries_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countries',
            options={'ordering': ('id',), 'verbose_name': 'Country'},
        ),
        migrations.AlterModelTable(
            name='countries',
            table=None,
        ),
    ]

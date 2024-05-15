# Generated by Django 5.0.6 on 2024-05-13 12:14
# This file is generated by makemigrations command, its name is default since i do not specify


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
# we specified this fields in models.py
    operations = [
        migrations.CreateModel(
            name='Countries', # do not change anything in migrations file
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('capital', models.CharField(default='', max_length=50)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]

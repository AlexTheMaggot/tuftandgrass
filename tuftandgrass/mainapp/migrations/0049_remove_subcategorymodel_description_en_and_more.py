# Generated by Django 4.0.4 on 2022-10-21 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0048_subcategorymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategorymodel',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='subcategorymodel',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='subcategorymodel',
            name='description_uz',
        ),
    ]

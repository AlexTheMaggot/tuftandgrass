# Generated by Django 4.0.4 on 2022-09-24 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0042_productimagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='available',
            field=models.BooleanField(default=1, verbose_name='Наличие'),
            preserve_default=False,
        ),
    ]

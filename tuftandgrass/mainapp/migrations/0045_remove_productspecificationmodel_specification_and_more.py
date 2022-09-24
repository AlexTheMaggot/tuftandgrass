# Generated by Django 4.0.4 on 2022-09-24 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0044_productspecificationmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productspecificationmodel',
            name='specification',
        ),
        migrations.RemoveField(
            model_name='productspecificationmodel',
            name='value',
        ),
        migrations.AddField(
            model_name='productspecificationmodel',
            name='specification_en',
            field=models.CharField(default=1, max_length=200, verbose_name='Характеристика на английском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productspecificationmodel',
            name='specification_ru',
            field=models.CharField(default=1, max_length=200, verbose_name='Характеристика на русском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productspecificationmodel',
            name='specification_uz',
            field=models.CharField(default=1, max_length=200, verbose_name='Характеристика на узбекском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productspecificationmodel',
            name='value_en',
            field=models.CharField(default=1, max_length=200, verbose_name='Значение на английском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productspecificationmodel',
            name='value_ru',
            field=models.CharField(default=1, max_length=200, verbose_name='Значение на русском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productspecificationmodel',
            name='value_uz',
            field=models.CharField(default=1, max_length=200, verbose_name='Значение на узбекском'),
            preserve_default=False,
        ),
    ]
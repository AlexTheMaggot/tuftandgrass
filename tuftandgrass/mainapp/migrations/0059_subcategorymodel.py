# Generated by Django 4.0.4 on 2023-01-31 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0058_collectionmodel_show_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubcategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200, verbose_name='Заголовок на русском')),
                ('title_en', models.CharField(max_length=200, verbose_name='Заголовок на английском')),
                ('title_uz', models.CharField(max_length=200, verbose_name='Заголовок на узбекском')),
                ('description_ru', models.TextField(verbose_name='Описание на русском')),
                ('description_en', models.TextField(verbose_name='Описание на английском')),
                ('description_uz', models.TextField(verbose_name='Описание на узбекском')),
                ('slug', models.SlugField(verbose_name='URL')),
                ('img', models.ImageField(upload_to='categories/', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subcategories', to='mainapp.categorymodel', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
    ]

# Generated by Django 4.0.4 on 2022-10-21 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0049_remove_subcategorymodel_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategorymodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='subcategories', to='mainapp.categorymodel', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='mainapp.subcategorymodel', verbose_name='Подкатегория'),
        ),
    ]

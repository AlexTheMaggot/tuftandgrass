# Generated by Django 4.0.4 on 2022-09-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0046_aboutpagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200, verbose_name='Заголовок на русском')),
                ('title_en', models.CharField(max_length=200, verbose_name='Заголовок на английском')),
                ('title_uz', models.CharField(max_length=200, verbose_name='Заголовок на узбекском')),
                ('description_ru', models.TextField(verbose_name='Описание на русском')),
                ('description_en', models.TextField(verbose_name='Описание на английском')),
                ('description_uz', models.TextField(verbose_name='Описание на узбекском')),
            ],
            options={
                'verbose_name': 'Страница контактов',
                'verbose_name_plural': 'Страница контактов',
            },
        ),
    ]
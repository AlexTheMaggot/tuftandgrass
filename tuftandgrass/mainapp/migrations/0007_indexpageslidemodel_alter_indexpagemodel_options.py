# Generated by Django 4.0.4 on 2022-09-14 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_indexpagemodel_worktime_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPageSlideModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='slides/')),
                ('first_title_ru', models.CharField(max_length=200)),
                ('first_title_en', models.CharField(max_length=200)),
                ('first_title_uz', models.CharField(max_length=200)),
                ('second_title_ru', models.CharField(max_length=200)),
                ('second_title_en', models.CharField(max_length=200)),
                ('second_title_uz', models.CharField(max_length=200)),
                ('description_ru', models.TextField()),
                ('description_en', models.TextField()),
                ('description_uz', models.TextField()),
            ],
            options={
                'verbose_name': 'Слайд главной страницы',
                'verbose_name_plural': 'Слайды главной страницы',
            },
        ),
        migrations.AlterModelOptions(
            name='indexpagemodel',
            options={'verbose_name': 'Главная страница', 'verbose_name_plural': 'Главная страница'},
        ),
    ]

# Generated by Django 4.0.4 on 2022-09-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_indexpagemodel_fifthblock_description_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPageTeamUnitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='teamunits/')),
                ('name_ru', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200)),
                ('name_uz', models.CharField(max_length=200)),
                ('position_ru', models.CharField(max_length=200)),
                ('position_en', models.CharField(max_length=200)),
                ('position_uz', models.CharField(max_length=200)),
                ('description_ru', models.TextField()),
                ('description_en', models.TextField()),
                ('description_uz', models.TextField()),
                ('facebook', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('telegram', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Участник команды',
                'verbose_name_plural': 'Команда',
            },
        ),
    ]

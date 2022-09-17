# Generated by Django 4.0.4 on 2022-09-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_indexpagemodel_secondblock_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpagemodel',
            name='thirdblock_description_en',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpagemodel',
            name='thirdblock_description_ru',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpagemodel',
            name='thirdblock_description_uz',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpagemodel',
            name='thirdblock_title_en',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpagemodel',
            name='thirdblock_title_ru',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpagemodel',
            name='thirdblock_title_uz',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

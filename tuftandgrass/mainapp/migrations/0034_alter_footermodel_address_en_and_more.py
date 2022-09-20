# Generated by Django 4.0.4 on 2022-09-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0033_subscribemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footermodel',
            name='address_en',
            field=models.CharField(max_length=200, verbose_name='Адрес на английском'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='address_ru',
            field=models.CharField(max_length=200, verbose_name='Адрес на русском'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='address_uz',
            field=models.CharField(max_length=200, verbose_name='Адрес на узбекском'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='description_en',
            field=models.TextField(verbose_name='Описание на английском'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='description_ru',
            field=models.TextField(verbose_name='Описание на русском'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='description_uz',
            field=models.TextField(verbose_name='Описание на узбекском'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='facebook',
            field=models.CharField(max_length=200, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='img',
            field=models.ImageField(upload_to='footer/', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='instagram',
            field=models.CharField(max_length=200, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='mail',
            field=models.CharField(max_length=200, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='mail_description_en',
            field=models.TextField(verbose_name='Подпись к почте на английском'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='mail_description_ru',
            field=models.TextField(verbose_name='Подпись к почте на русском'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='mail_description_uz',
            field=models.TextField(verbose_name='Подпись к почте на узбекском'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='phone',
            field=models.CharField(max_length=200, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='telegram',
            field=models.CharField(max_length=200, verbose_name='Telegram'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='website',
            field=models.CharField(max_length=200, verbose_name='Сайт'),
        ),
        migrations.AlterField(
            model_name='footermodel',
            name='youtube',
            field=models.CharField(max_length=200, verbose_name='Youtube'),
        ),
        migrations.AlterField(
            model_name='headermodel',
            name='img',
            field=models.ImageField(upload_to='header/', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='indexpagefaqmodel',
            name='answer_en',
            field=models.TextField(verbose_name='Ответ на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagefaqmodel',
            name='answer_ru',
            field=models.TextField(verbose_name='Ответ на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagefaqmodel',
            name='answer_uz',
            field=models.TextField(verbose_name='Ответ на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagefaqmodel',
            name='question_en',
            field=models.CharField(max_length=200, verbose_name='Вопрос на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagefaqmodel',
            name='question_ru',
            field=models.CharField(max_length=200, verbose_name='Вопрос на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagefaqmodel',
            name='question_uz',
            field=models.CharField(max_length=200, verbose_name='Вопрос на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='address_en',
            field=models.CharField(max_length=200, verbose_name='Адрес на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='address_ru',
            field=models.CharField(max_length=200, verbose_name='Адрес на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='address_uz',
            field=models.CharField(max_length=200, verbose_name='Адрес на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='copyright_en',
            field=models.CharField(max_length=200, verbose_name='Копирайт на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='copyright_ru',
            field=models.CharField(max_length=200, verbose_name='Копирайт на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='copyright_uz',
            field=models.CharField(max_length=200, verbose_name='Копирайт на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='description_en',
            field=models.TextField(verbose_name='Описание страницы на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='description_ru',
            field=models.TextField(verbose_name='Описание страницы на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='description_uz',
            field=models.TextField(verbose_name='Описание страницы на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='eighthblock_description_en',
            field=models.TextField(verbose_name='Текст восьмого блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='eighthblock_description_ru',
            field=models.TextField(verbose_name='Текст восьмого блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='eighthblock_description_uz',
            field=models.TextField(verbose_name='Текст восьмого блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='eighthblock_title_en',
            field=models.CharField(max_length=200, verbose_name='Заголовок восьмого блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='eighthblock_title_ru',
            field=models.CharField(max_length=200, verbose_name='Заголовок восьмого блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='eighthblock_title_uz',
            field=models.CharField(max_length=200, verbose_name='Заголовок восьмого блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='facebook',
            field=models.CharField(max_length=200, verbose_name='Ссылка на Facebook'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fifthblock_description_en',
            field=models.TextField(verbose_name='Текст пятого блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fifthblock_description_ru',
            field=models.TextField(verbose_name='Текст пятого блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fifthblock_description_uz',
            field=models.TextField(verbose_name='Текст пятого блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fifthblock_title_en',
            field=models.CharField(max_length=200, verbose_name='Заголовок пятого блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fifthblock_title_ru',
            field=models.CharField(max_length=200, verbose_name='Заголовок пятого блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fifthblock_title_uz',
            field=models.CharField(max_length=200, verbose_name='Заголовок пятого блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fourthblock_description_en',
            field=models.TextField(verbose_name='Текст четвертого блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fourthblock_description_ru',
            field=models.TextField(verbose_name='Текст четвертого блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fourthblock_description_uz',
            field=models.TextField(verbose_name='Текст четвертого блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fourthblock_img',
            field=models.ImageField(upload_to='indexpage/', verbose_name='Изоражение четвертого блока'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fourthblock_title_en',
            field=models.CharField(max_length=200, verbose_name='Заголовок четвертого блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fourthblock_title_ru',
            field=models.CharField(max_length=200, verbose_name='Заголовок четвертого блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='fourthblock_title_uz',
            field=models.CharField(max_length=200, verbose_name='Заголовок четвертого блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='ninthblock_description_en',
            field=models.TextField(verbose_name='Текст девятого блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='ninthblock_description_ru',
            field=models.TextField(verbose_name='Текст девятого блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='ninthblock_description_uz',
            field=models.TextField(verbose_name='Текст девятого блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='ninthblock_title_en',
            field=models.CharField(max_length=200, verbose_name='Заголовок девятого блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='ninthblock_title_ru',
            field=models.CharField(max_length=200, verbose_name='Заголовок девятого блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='ninthblock_title_uz',
            field=models.CharField(max_length=200, verbose_name='Заголовок девятого блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='phone',
            field=models.CharField(max_length=200, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_description_en',
            field=models.TextField(verbose_name='Текст второго блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_description_ru',
            field=models.TextField(verbose_name='Текст второго блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_description_uz',
            field=models.TextField(verbose_name='Текст второго блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_1_en',
            field=models.CharField(max_length=200, verbose_name='Первое преимущество на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_1_ru',
            field=models.CharField(max_length=200, verbose_name='Первое преимущество на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_1_uz',
            field=models.CharField(max_length=200, verbose_name='Первое преимущество на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_2_en',
            field=models.CharField(max_length=200, verbose_name='Второе преимущество на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_2_ru',
            field=models.CharField(max_length=200, verbose_name='Второе преимущество на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_2_uz',
            field=models.CharField(max_length=200, verbose_name='Второе преимущество на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_3_en',
            field=models.CharField(max_length=200, verbose_name='Третье преимущество на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_3_ru',
            field=models.CharField(max_length=200, verbose_name='Третье преимущество на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_3_uz',
            field=models.CharField(max_length=200, verbose_name='Третье преимущество на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_4_en',
            field=models.CharField(max_length=200, verbose_name='Четвертое преимущество на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_4_ru',
            field=models.CharField(max_length=200, verbose_name='Четвертое преимущество на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_4_uz',
            field=models.CharField(max_length=200, verbose_name='Четвертое преимущество на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_5_en',
            field=models.CharField(max_length=200, verbose_name='Пятое преимущество на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_5_ru',
            field=models.CharField(max_length=200, verbose_name='Пятое преимущество на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_5_uz',
            field=models.CharField(max_length=200, verbose_name='Пятое преимущество на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_6_en',
            field=models.CharField(max_length=200, verbose_name='Шестое преимущество на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_6_ru',
            field=models.CharField(max_length=200, verbose_name='Шестое преимущество на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_feature_6_uz',
            field=models.CharField(max_length=200, verbose_name='Шестое преимущество на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_img',
            field=models.ImageField(upload_to='indexpage/', verbose_name='Картинка для второго блока'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_link',
            field=models.CharField(max_length=200, verbose_name='Ссылка для второго блока'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_subtitle_en',
            field=models.CharField(max_length=200, verbose_name='Подзаголовок второго блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_subtitle_ru',
            field=models.CharField(max_length=200, verbose_name='Подзаголовок второго блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_subtitle_uz',
            field=models.CharField(max_length=200, verbose_name='Подзаголовок второго блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_title_en',
            field=models.CharField(max_length=200, verbose_name='Заголовок второго блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_title_ru',
            field=models.CharField(max_length=200, verbose_name='Заголовок второго блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='secondblock_title_uz',
            field=models.CharField(max_length=200, verbose_name='Заголовок второго блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='telegram',
            field=models.CharField(max_length=200, verbose_name='Ссылка на Telegram'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='thirdblock_description_en',
            field=models.TextField(verbose_name='Текст третьего блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='thirdblock_description_ru',
            field=models.TextField(verbose_name='Текст третьего блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='thirdblock_description_uz',
            field=models.TextField(verbose_name='Текст третьего блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='thirdblock_title_en',
            field=models.CharField(max_length=200, verbose_name='Заголовок третьего блока на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='thirdblock_title_ru',
            field=models.CharField(max_length=200, verbose_name='Заголовок третьего блока на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='thirdblock_title_uz',
            field=models.CharField(max_length=200, verbose_name='Заголовок третьего блока на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='title_en',
            field=models.CharField(max_length=200, verbose_name='Заголовок страницы на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='title_ru',
            field=models.CharField(max_length=200, verbose_name='Заголовок страницы на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='title_uz',
            field=models.CharField(max_length=200, verbose_name='Заголовок страницы на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='worktime_en',
            field=models.CharField(max_length=200, verbose_name='Время работы на английском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='worktime_ru',
            field=models.CharField(max_length=200, verbose_name='Время работы на русском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='worktime_uz',
            field=models.CharField(max_length=200, verbose_name='Время работы на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpagemodel',
            name='youtube',
            field=models.CharField(max_length=200, verbose_name='Ссылка на Youtube'),
        ),
        migrations.AlterField(
            model_name='indexpageproductmodel',
            name='description_en',
            field=models.TextField(verbose_name='Описание на английском'),
        ),
        migrations.AlterField(
            model_name='indexpageproductmodel',
            name='description_ru',
            field=models.TextField(verbose_name='Описание на русском'),
        ),
        migrations.AlterField(
            model_name='indexpageproductmodel',
            name='description_uz',
            field=models.TextField(verbose_name='Описание на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpageproductmodel',
            name='img',
            field=models.ImageField(upload_to='indexpage_products/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='indexpageproductmodel',
            name='link',
            field=models.CharField(max_length=200, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='indexpageproductmodel',
            name='title_en',
            field=models.CharField(max_length=200, verbose_name='Заголовок на английском'),
        ),
        migrations.AlterField(
            model_name='indexpageproductmodel',
            name='title_ru',
            field=models.CharField(max_length=200, verbose_name='Заголовок на русском'),
        ),
        migrations.AlterField(
            model_name='indexpageproductmodel',
            name='title_uz',
            field=models.CharField(max_length=200, verbose_name='Заголовок на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpageslidemodel',
            name='description_en',
            field=models.TextField(verbose_name='Описание на английском'),
        ),
        migrations.AlterField(
            model_name='indexpageslidemodel',
            name='description_ru',
            field=models.TextField(verbose_name='Описание на русском'),
        ),
        migrations.AlterField(
            model_name='indexpageslidemodel',
            name='description_uz',
            field=models.TextField(verbose_name='Описание на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpageslidemodel',
            name='first_title_en',
            field=models.CharField(max_length=200, verbose_name='Первая часть заголовка на английском'),
        ),
        migrations.AlterField(
            model_name='indexpageslidemodel',
            name='first_title_ru',
            field=models.CharField(max_length=200, verbose_name='Первая часть заголовка на русском'),
        ),
        migrations.AlterField(
            model_name='indexpageslidemodel',
            name='first_title_uz',
            field=models.CharField(max_length=200, verbose_name='Первая часть заголовка на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpageslidemodel',
            name='img',
            field=models.ImageField(upload_to='slides/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='indexpageslidemodel',
            name='link',
            field=models.CharField(max_length=200, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='indexpageslidemodel',
            name='second_title_en',
            field=models.CharField(max_length=200, verbose_name='Вторая часть заголовка на английском'),
        ),
        migrations.AlterField(
            model_name='indexpageslidemodel',
            name='second_title_ru',
            field=models.CharField(max_length=200, verbose_name='Вторая часть заголовка на русском'),
        ),
        migrations.AlterField(
            model_name='indexpageslidemodel',
            name='second_title_uz',
            field=models.CharField(max_length=200, verbose_name='Вторая часть заголовка на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='description_en',
            field=models.TextField(verbose_name='Описание на английском'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='description_ru',
            field=models.TextField(verbose_name='Описание на русском'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='description_uz',
            field=models.TextField(verbose_name='Описание на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='facebook',
            field=models.CharField(max_length=200, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='img',
            field=models.ImageField(upload_to='teamunits/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='instagram',
            field=models.CharField(max_length=200, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='name_en',
            field=models.CharField(max_length=200, verbose_name='Имя на английском'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='name_ru',
            field=models.CharField(max_length=200, verbose_name='Имя на русском'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='name_uz',
            field=models.CharField(max_length=200, verbose_name='Имя на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='position_en',
            field=models.CharField(max_length=200, verbose_name='Должность на английском'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='position_ru',
            field=models.CharField(max_length=200, verbose_name='Должность на русском'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='position_uz',
            field=models.CharField(max_length=200, verbose_name='Должность на узбекском'),
        ),
        migrations.AlterField(
            model_name='indexpageteamunitmodel',
            name='telegram',
            field=models.CharField(max_length=200, verbose_name='Telegram'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='date',
            field=models.DateField(verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='description_en',
            field=models.TextField(verbose_name='Описание на английском'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='description_ru',
            field=models.TextField(verbose_name='Описание на русском'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='description_uz',
            field=models.TextField(verbose_name='Описание на узбекском'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='img',
            field=models.ImageField(upload_to='news/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='title_en',
            field=models.CharField(max_length=200, verbose_name='Заголовок на английском'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='title_ru',
            field=models.CharField(max_length=200, verbose_name='Заголовок на русском'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='title_uz',
            field=models.CharField(max_length=200, verbose_name='Заголовок на узбекском'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='phone',
            field=models.CharField(max_length=200, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='img',
            field=models.ImageField(upload_to='reviews/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='name_en',
            field=models.CharField(max_length=200, verbose_name='Имя на английском'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='name_ru',
            field=models.CharField(max_length=200, verbose_name='Имя на русском'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='name_uz',
            field=models.CharField(max_length=200, verbose_name='Имя на узбекском'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='position_en',
            field=models.CharField(max_length=200, verbose_name='Должность на английском'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='position_ru',
            field=models.CharField(max_length=200, verbose_name='Должность на русском'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='position_uz',
            field=models.CharField(max_length=200, verbose_name='Должность на узбекском'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='text_en',
            field=models.TextField(verbose_name='Текст на английском'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='text_ru',
            field=models.TextField(verbose_name='Текст на русском'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='text_uz',
            field=models.TextField(verbose_name='Текст на узбекском'),
        ),
        migrations.AlterField(
            model_name='subscribemodel',
            name='email',
            field=models.CharField(max_length=200, verbose_name='E-mail'),
        ),
    ]

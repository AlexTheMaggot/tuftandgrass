from django.db import models


class IndexPageModel(models.Model):
    title_ru = models.CharField(max_length=200)
    title_uz = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    description_ru = models.TextField()
    description_uz = models.TextField()
    description_en = models.TextField()
    facebook = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)
    youtube = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address_ru = models.CharField(max_length=200)
    address_en = models.CharField(max_length=200)
    address_uz = models.CharField(max_length=200)
    worktime_ru = models.CharField(max_length=200)
    worktime_en = models.CharField(max_length=200)
    worktime_uz = models.CharField(max_length=200)
    secondblock_img = models.ImageField(upload_to='indexpage/')
    secondblock_link = models.CharField(max_length=200)
    secondblock_title_ru = models.CharField(max_length=200)
    secondblock_title_en = models.CharField(max_length=200)
    secondblock_title_uz = models.CharField(max_length=200)
    secondblock_subtitle_ru = models.CharField(max_length=200)
    secondblock_subtitle_en = models.CharField(max_length=200)
    secondblock_subtitle_uz = models.CharField(max_length=200)
    secondblock_description_ru = models.TextField()
    secondblock_description_en = models.TextField()
    secondblock_description_uz = models.TextField()
    secondblock_feature_1_ru = models.CharField(max_length=200)
    secondblock_feature_1_en = models.CharField(max_length=200)
    secondblock_feature_1_uz = models.CharField(max_length=200)
    secondblock_feature_2_ru = models.CharField(max_length=200)
    secondblock_feature_2_en = models.CharField(max_length=200)
    secondblock_feature_2_uz = models.CharField(max_length=200)
    secondblock_feature_3_ru = models.CharField(max_length=200)
    secondblock_feature_3_en = models.CharField(max_length=200)
    secondblock_feature_3_uz = models.CharField(max_length=200)
    secondblock_feature_4_ru = models.CharField(max_length=200)
    secondblock_feature_4_en = models.CharField(max_length=200)
    secondblock_feature_4_uz = models.CharField(max_length=200)
    secondblock_feature_5_ru = models.CharField(max_length=200)
    secondblock_feature_5_en = models.CharField(max_length=200)
    secondblock_feature_5_uz = models.CharField(max_length=200)
    secondblock_feature_6_ru = models.CharField(max_length=200)
    secondblock_feature_6_en = models.CharField(max_length=200)
    secondblock_feature_6_uz = models.CharField(max_length=200)
    thirdblock_title_ru = models.CharField(max_length=200)
    thirdblock_title_en = models.CharField(max_length=200)
    thirdblock_title_uz = models.CharField(max_length=200)
    thirdblock_description_ru = models.TextField()
    thirdblock_description_en = models.TextField()
    thirdblock_description_uz = models.TextField()
    fourthblock_img = models.ImageField(upload_to='indexpage/')
    fourthblock_title_ru = models.CharField(max_length=200)
    fourthblock_title_en = models.CharField(max_length=200)
    fourthblock_title_uz = models.CharField(max_length=200)
    fourthblock_description_ru = models.TextField()
    fourthblock_description_en = models.TextField()
    fourthblock_description_uz = models.TextField()
    fifthblock_title_ru = models.CharField(max_length=200)
    fifthblock_title_en = models.CharField(max_length=200)
    fifthblock_title_uz = models.CharField(max_length=200)
    fifthblock_description_ru = models.TextField()
    fifthblock_description_en = models.TextField()
    fifthblock_description_uz = models.TextField()
    eighthblock_title_ru = models.CharField(max_length=200)
    eighthblock_title_en = models.CharField(max_length=200)
    eighthblock_title_uz = models.CharField(max_length=200)
    eighthblock_description_ru = models.TextField()
    eighthblock_description_en = models.TextField()
    eighthblock_description_uz = models.TextField()
    ninthblock_title_ru = models.CharField(max_length=200)
    ninthblock_title_en = models.CharField(max_length=200)
    ninthblock_title_uz = models.CharField(max_length=200)
    ninthblock_description_ru = models.TextField()
    ninthblock_description_en = models.TextField()
    ninthblock_description_uz = models.TextField()
    copyright_ru = models.CharField(max_length=200)
    copyright_en = models.CharField(max_length=200)
    copyright_uz = models.CharField(max_length=200)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class IndexPageSlideModel(models.Model):
    img = models.ImageField(upload_to='slides/')
    link = models.CharField(max_length=200)
    first_title_ru = models.CharField(max_length=200)
    first_title_en = models.CharField(max_length=200)
    first_title_uz = models.CharField(max_length=200)
    second_title_ru = models.CharField(max_length=200)
    second_title_en = models.CharField(max_length=200)
    second_title_uz = models.CharField(max_length=200)
    description_ru = models.TextField()
    description_en = models.TextField()
    description_uz = models.TextField()

    def __str__(self):
        return self.first_title_ru

    class Meta:
        verbose_name = 'Слайд главной страницы'
        verbose_name_plural = 'Слайды главной страницы'


class IndexPageProductModel(models.Model):
    img = models.ImageField(upload_to='indexpage_products/')
    link = models.CharField(max_length=200)
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_uz = models.CharField(max_length=200)
    description_ru = models.TextField()
    description_en = models.TextField()
    description_uz = models.TextField()

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Продукт главной страницы'
        verbose_name_plural = 'Продукты главной страницы'


class IndexPageFAQModel(models.Model):
    question_ru = models.CharField(max_length=200)
    question_en = models.CharField(max_length=200)
    question_uz = models.CharField(max_length=200)
    answer_ru = models.TextField()
    answer_en = models.TextField()
    answer_uz = models.TextField()

    def __str__(self):
        return self.question_ru

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'


class IndexPageTeamUnitModel(models.Model):
    img = models.ImageField(upload_to='teamunits/')
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    name_uz = models.CharField(max_length=200)
    position_ru = models.CharField(max_length=200)
    position_en = models.CharField(max_length=200)
    position_uz = models.CharField(max_length=200)
    description_ru = models.TextField()
    description_en = models.TextField()
    description_uz = models.TextField()
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Участник команды'
        verbose_name_plural = 'Команда'


class OrderModel(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class ReviewModel(models.Model):
    img = models.ImageField(upload_to='reviews/')
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    name_uz = models.CharField(max_length=200)
    position_ru = models.CharField(max_length=200)
    position_en = models.CharField(max_length=200)
    position_uz = models.CharField(max_length=200)
    text_ru = models.TextField()
    text_en = models.TextField()
    text_uz = models.TextField()

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class NewsModel(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_uz = models.CharField(max_length=200)
    description_ru = models.TextField()
    description_en = models.TextField()
    description_uz = models.TextField()
    img = models.ImageField(upload_to='news/')
    date = models.DateField()

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class HeaderModel(models.Model):
    img = models.ImageField(upload_to='header/')

    def __str__(self):
        return 'Шапка сайта'

    class Meta:
        verbose_name = 'Шапка сайта'
        verbose_name_plural = 'Шапка сайта'


class FooterModel(models.Model):
    img = models.ImageField(upload_to='footer/')
    description_ru = models.TextField()
    description_en = models.TextField()
    description_uz = models.TextField()
    address_ru = models.CharField(max_length=200)
    address_en = models.CharField(max_length=200)
    address_uz = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    mail_description_ru = models.TextField()
    mail_description_en = models.TextField()
    mail_description_uz = models.TextField()
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)
    youtube = models.CharField(max_length=200)

    def __str__(self):
        return 'Подвал сайта'

    class Meta:
        verbose_name = 'Подвал сайта'
        verbose_name_plural = 'Подвал сайта'


class SubscribeModel(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписка'

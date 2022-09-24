from django.db import models


class IndexPageModel(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Заголовок страницы на русском')
    title_uz = models.CharField(max_length=200, verbose_name='Заголовок страницы на узбекском')
    title_en = models.CharField(max_length=200, verbose_name='Заголовок страницы на английском')
    description_ru = models.TextField(verbose_name='Описание страницы на русском')
    description_uz = models.TextField(verbose_name='Описание страницы на узбекском')
    description_en = models.TextField(verbose_name='Описание страницы на английском')
    facebook = models.CharField(max_length=200, verbose_name='Ссылка на Facebook')
    telegram = models.CharField(max_length=200, verbose_name='Ссылка на Telegram')
    youtube = models.CharField(max_length=200, verbose_name='Ссылка на Youtube')
    phone = models.CharField(max_length=200, verbose_name='Номер телефона')
    address_ru = models.CharField(max_length=200, verbose_name='Адрес на русском')
    address_en = models.CharField(max_length=200, verbose_name='Адрес на английском')
    address_uz = models.CharField(max_length=200, verbose_name='Адрес на узбекском')
    worktime_ru = models.CharField(max_length=200, verbose_name='Время работы на русском')
    worktime_en = models.CharField(max_length=200, verbose_name='Время работы на английском')
    worktime_uz = models.CharField(max_length=200, verbose_name='Время работы на узбекском')
    secondblock_img = models.ImageField(upload_to='indexpage/', verbose_name='Картинка для второго блока')
    secondblock_link = models.CharField(max_length=200, verbose_name='Ссылка для второго блока')
    secondblock_title_ru = models.CharField(max_length=200, verbose_name='Заголовок второго блока на русском')
    secondblock_title_en = models.CharField(max_length=200, verbose_name='Заголовок второго блока на английском')
    secondblock_title_uz = models.CharField(max_length=200, verbose_name='Заголовок второго блока на узбекском')
    secondblock_subtitle_ru = models.CharField(max_length=200, verbose_name='Подзаголовок второго блока на русском')
    secondblock_subtitle_en = models.CharField(max_length=200, verbose_name='Подзаголовок второго блока на английском')
    secondblock_subtitle_uz = models.CharField(max_length=200, verbose_name='Подзаголовок второго блока на узбекском')
    secondblock_description_ru = models.TextField(verbose_name='Текст второго блока на русском')
    secondblock_description_en = models.TextField(verbose_name='Текст второго блока на английском')
    secondblock_description_uz = models.TextField(verbose_name='Текст второго блока на узбекском')
    secondblock_feature_1_ru = models.CharField(max_length=200, verbose_name='Первое преимущество на русском')
    secondblock_feature_1_en = models.CharField(max_length=200, verbose_name='Первое преимущество на английском')
    secondblock_feature_1_uz = models.CharField(max_length=200, verbose_name='Первое преимущество на узбекском')
    secondblock_feature_2_ru = models.CharField(max_length=200, verbose_name='Второе преимущество на русском')
    secondblock_feature_2_en = models.CharField(max_length=200, verbose_name='Второе преимущество на английском')
    secondblock_feature_2_uz = models.CharField(max_length=200, verbose_name='Второе преимущество на узбекском')
    secondblock_feature_3_ru = models.CharField(max_length=200, verbose_name='Третье преимущество на русском')
    secondblock_feature_3_en = models.CharField(max_length=200, verbose_name='Третье преимущество на английском')
    secondblock_feature_3_uz = models.CharField(max_length=200, verbose_name='Третье преимущество на узбекском')
    secondblock_feature_4_ru = models.CharField(max_length=200, verbose_name='Четвертое преимущество на русском')
    secondblock_feature_4_en = models.CharField(max_length=200, verbose_name='Четвертое преимущество на английском')
    secondblock_feature_4_uz = models.CharField(max_length=200, verbose_name='Четвертое преимущество на узбекском')
    secondblock_feature_5_ru = models.CharField(max_length=200, verbose_name='Пятое преимущество на русском')
    secondblock_feature_5_en = models.CharField(max_length=200, verbose_name='Пятое преимущество на английском')
    secondblock_feature_5_uz = models.CharField(max_length=200, verbose_name='Пятое преимущество на узбекском')
    secondblock_feature_6_ru = models.CharField(max_length=200, verbose_name='Шестое преимущество на русском')
    secondblock_feature_6_en = models.CharField(max_length=200, verbose_name='Шестое преимущество на английском')
    secondblock_feature_6_uz = models.CharField(max_length=200, verbose_name='Шестое преимущество на узбекском')
    thirdblock_title_ru = models.CharField(max_length=200, verbose_name='Заголовок третьего блока на русском')
    thirdblock_title_en = models.CharField(max_length=200, verbose_name='Заголовок третьего блока на английском')
    thirdblock_title_uz = models.CharField(max_length=200, verbose_name='Заголовок третьего блока на узбекском')
    thirdblock_description_ru = models.TextField(verbose_name='Текст третьего блока на русском')
    thirdblock_description_en = models.TextField(verbose_name='Текст третьего блока на английском')
    thirdblock_description_uz = models.TextField(verbose_name='Текст третьего блока на узбекском')
    fourthblock_img = models.ImageField(upload_to='indexpage/', verbose_name='Изоражение четвертого блока')
    fourthblock_title_ru = models.CharField(max_length=200, verbose_name='Заголовок четвертого блока на русском')
    fourthblock_title_en = models.CharField(max_length=200, verbose_name='Заголовок четвертого блока на английском')
    fourthblock_title_uz = models.CharField(max_length=200, verbose_name='Заголовок четвертого блока на узбекском')
    fourthblock_description_ru = models.TextField(verbose_name='Текст четвертого блока на русском')
    fourthblock_description_en = models.TextField(verbose_name='Текст четвертого блока на английском')
    fourthblock_description_uz = models.TextField(verbose_name='Текст четвертого блока на узбекском')
    fifthblock_title_ru = models.CharField(max_length=200, verbose_name='Заголовок пятого блока на русском')
    fifthblock_title_en = models.CharField(max_length=200, verbose_name='Заголовок пятого блока на английском')
    fifthblock_title_uz = models.CharField(max_length=200, verbose_name='Заголовок пятого блока на узбекском')
    fifthblock_description_ru = models.TextField(verbose_name='Текст пятого блока на русском')
    fifthblock_description_en = models.TextField(verbose_name='Текст пятого блока на английском')
    fifthblock_description_uz = models.TextField(verbose_name='Текст пятого блока на узбекском')
    eighthblock_title_ru = models.CharField(max_length=200, verbose_name='Заголовок восьмого блока на русском')
    eighthblock_title_en = models.CharField(max_length=200, verbose_name='Заголовок восьмого блока на английском')
    eighthblock_title_uz = models.CharField(max_length=200, verbose_name='Заголовок восьмого блока на узбекском')
    eighthblock_description_ru = models.TextField(verbose_name='Текст восьмого блока на русском')
    eighthblock_description_en = models.TextField(verbose_name='Текст восьмого блока на английском')
    eighthblock_description_uz = models.TextField(verbose_name='Текст восьмого блока на узбекском')
    ninthblock_title_ru = models.CharField(max_length=200, verbose_name='Заголовок девятого блока на русском')
    ninthblock_title_en = models.CharField(max_length=200, verbose_name='Заголовок девятого блока на английском')
    ninthblock_title_uz = models.CharField(max_length=200, verbose_name='Заголовок девятого блока на узбекском')
    ninthblock_description_ru = models.TextField(verbose_name='Текст девятого блока на русском')
    ninthblock_description_en = models.TextField(verbose_name='Текст девятого блока на английском')
    ninthblock_description_uz = models.TextField(verbose_name='Текст девятого блока на узбекском')
    copyright_ru = models.CharField(max_length=200, verbose_name='Копирайт на русском')
    copyright_en = models.CharField(max_length=200, verbose_name='Копирайт на английском')
    copyright_uz = models.CharField(max_length=200, verbose_name='Копирайт на узбекском')

    def __str__(self):
        return 'Главная страница'

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class NewsListPageModel(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Заголовок на русском')
    title_en = models.CharField(max_length=200, verbose_name='Заголовок на английском')
    title_uz = models.CharField(max_length=200, verbose_name='Заголовок на узбекском')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_uz = models.TextField(verbose_name='Описание на узбекском')

    def __str__(self):
        return 'Страница списка новостей'

    class Meta:
        verbose_name = 'Страница списка новостей'
        verbose_name_plural = 'Страница списка новостей'


class IndexPageSlideModel(models.Model):
    img = models.ImageField(upload_to='slides/', verbose_name='Изображение')
    link = models.CharField(max_length=200, verbose_name='Ссылка')
    first_title_ru = models.CharField(max_length=200, verbose_name='Первая часть заголовка на русском')
    first_title_en = models.CharField(max_length=200, verbose_name='Первая часть заголовка на английском')
    first_title_uz = models.CharField(max_length=200, verbose_name='Первая часть заголовка на узбекском')
    second_title_ru = models.CharField(max_length=200, verbose_name='Вторая часть заголовка на русском')
    second_title_en = models.CharField(max_length=200, verbose_name='Вторая часть заголовка на английском')
    second_title_uz = models.CharField(max_length=200, verbose_name='Вторая часть заголовка на узбекском')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_uz = models.TextField(verbose_name='Описание на узбекском')

    def __str__(self):
        return self.first_title_ru

    class Meta:
        verbose_name = 'Слайд главной страницы'
        verbose_name_plural = 'Слайды главной страницы'


class IndexPageProductModel(models.Model):
    img = models.ImageField(upload_to='indexpage_products/', verbose_name='Изображение')
    link = models.CharField(max_length=200, verbose_name='Ссылка')
    title_ru = models.CharField(max_length=200, verbose_name='Заголовок на русском')
    title_en = models.CharField(max_length=200, verbose_name='Заголовок на английском')
    title_uz = models.CharField(max_length=200, verbose_name='Заголовок на узбекском')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_uz = models.TextField(verbose_name='Описание на узбекском')

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Продукт главной страницы'
        verbose_name_plural = 'Продукты главной страницы'


class IndexPageFAQModel(models.Model):
    question_ru = models.CharField(max_length=200, verbose_name='Вопрос на русском')
    question_en = models.CharField(max_length=200, verbose_name='Вопрос на английском')
    question_uz = models.CharField(max_length=200, verbose_name='Вопрос на узбекском')
    answer_ru = models.TextField(verbose_name='Ответ на русском')
    answer_en = models.TextField(verbose_name='Ответ на английском')
    answer_uz = models.TextField(verbose_name='Ответ на узбекском')

    def __str__(self):
        return self.question_ru

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'


class IndexPageTeamUnitModel(models.Model):
    img = models.ImageField(upload_to='teamunits/', verbose_name='Изображение')
    name_ru = models.CharField(max_length=200, verbose_name='Имя на русском')
    name_en = models.CharField(max_length=200, verbose_name='Имя на английском')
    name_uz = models.CharField(max_length=200, verbose_name='Имя на узбекском')
    position_ru = models.CharField(max_length=200, verbose_name='Должность на русском')
    position_en = models.CharField(max_length=200, verbose_name='Должность на английском')
    position_uz = models.CharField(max_length=200, verbose_name='Должность на узбекском')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_uz = models.TextField(verbose_name='Описание на узбекском')
    facebook = models.CharField(max_length=200, verbose_name='Facebook')
    instagram = models.CharField(max_length=200, verbose_name='Instagram')
    telegram = models.CharField(max_length=200, verbose_name='Telegram')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Участник команды'
        verbose_name_plural = 'Команда'


class OrderModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=200, verbose_name='Номер телефона')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='E-mail')
    text = models.TextField(null=True, blank=True, verbose_name='Текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class ReviewModel(models.Model):
    img = models.ImageField(upload_to='reviews/', verbose_name='Изображение')
    name_ru = models.CharField(max_length=200, verbose_name='Имя на русском')
    name_en = models.CharField(max_length=200, verbose_name='Имя на английском')
    name_uz = models.CharField(max_length=200, verbose_name='Имя на узбекском')
    position_ru = models.CharField(max_length=200, verbose_name='Должность на русском')
    position_en = models.CharField(max_length=200, verbose_name='Должность на английском')
    position_uz = models.CharField(max_length=200, verbose_name='Должность на узбекском')
    text_ru = models.TextField(verbose_name='Текст на русском')
    text_en = models.TextField(verbose_name='Текст на английском')
    text_uz = models.TextField(verbose_name='Текст на узбекском')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class NewsModel(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Заголовок на русском')
    title_en = models.CharField(max_length=200, verbose_name='Заголовок на английском')
    title_uz = models.CharField(max_length=200, verbose_name='Заголовок на узбекском')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_uz = models.TextField(verbose_name='Описание на узбекском')
    img = models.ImageField(upload_to='news/', verbose_name='Изображение')
    date = models.DateField(verbose_name='Дата создания')
    text_ru = models.TextField(verbose_name='Текст на русском')
    text_en = models.TextField(verbose_name='Текст на английском')
    text_uz = models.TextField(verbose_name='Текст на узбекском')

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class HeaderModel(models.Model):
    img = models.ImageField(upload_to='header/', verbose_name='Логотип')

    def __str__(self):
        return 'Шапка сайта'

    class Meta:
        verbose_name = 'Шапка сайта'
        verbose_name_plural = 'Шапка сайта'


class FooterModel(models.Model):
    img = models.ImageField(upload_to='footer/', verbose_name='Логотип')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_uz = models.TextField(verbose_name='Описание на узбекском')
    address_ru = models.CharField(max_length=200, verbose_name='Адрес на русском')
    address_en = models.CharField(max_length=200, verbose_name='Адрес на английском')
    address_uz = models.CharField(max_length=200, verbose_name='Адрес на узбекском')
    phone = models.CharField(max_length=200, verbose_name='Номер телефона')
    mail = models.CharField(max_length=200, verbose_name='E-mail')
    website = models.CharField(max_length=200, verbose_name='Сайт')
    mail_description_ru = models.TextField(verbose_name='Подпись к почте на русском')
    mail_description_en = models.TextField(verbose_name='Подпись к почте на английском')
    mail_description_uz = models.TextField(verbose_name='Подпись к почте на узбекском')
    facebook = models.CharField(max_length=200, verbose_name='Facebook')
    instagram = models.CharField(max_length=200, verbose_name='Instagram')
    telegram = models.CharField(max_length=200, verbose_name='Telegram')
    youtube = models.CharField(max_length=200, verbose_name='Youtube')

    def __str__(self):
        return 'Подвал сайта'

    class Meta:
        verbose_name = 'Подвал сайта'
        verbose_name_plural = 'Подвал сайта'


class SubscribeModel(models.Model):
    email = models.CharField(max_length=200, verbose_name='E-mail')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписка'


class CategoryListPageModel(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Заголовок на русском')
    title_en = models.CharField(max_length=200, verbose_name='Заголовок на английском')
    title_uz = models.CharField(max_length=200, verbose_name='Заголовок на узбекском')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_uz = models.TextField(verbose_name='Описание на узбекском')

    def __str__(self):
        return 'Страница каталога'

    class Meta:
        verbose_name = 'Страница каталога'
        verbose_name_plural = 'Страница каталога'


class CategoryModel(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Заголовок на русском')
    title_en = models.CharField(max_length=200, verbose_name='Заголовок на английском')
    title_uz = models.CharField(max_length=200, verbose_name='Заголовок на узбекском')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_uz = models.TextField(verbose_name='Описание на узбекском')
    slug = models.SlugField(verbose_name='URL')
    img = models.ImageField(upload_to='categories/', verbose_name='Изображение')

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ProductModel(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Заголовок на русском')
    title_en = models.CharField(max_length=200, verbose_name='Заголовок на английском')
    title_uz = models.CharField(max_length=200, verbose_name='Заголовок на узбекском')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_uz = models.TextField(verbose_name='Описание на узбекском')
    slug = models.SlugField(verbose_name='URL')
    img = models.ImageField(upload_to='categories/', verbose_name='Изображение')
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Категория'
    )
    price = models.IntegerField(verbose_name='Цена')
    new = models.BooleanField(verbose_name='Новинка')

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImageModel(models.Model):
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='product_images',
        verbose_name='Продукт'
    )
    img = models.ImageField(upload_to='product_images/', verbose_name='Изображение')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продукта'

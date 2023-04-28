from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Doctype
class Doctype(models.Model):
    doctype_name = models.CharField(verbose_name='Тип документа', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.doctype_name

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Тип документы'


# Document
class Document(models.Model):
    title = models.CharField(verbose_name='Тип документа', max_length=255)
    doctype = models.ForeignKey(Doctype, on_delete=models.CASCADE, verbose_name='Тип документа')
    source = models.FileField(verbose_name='Исходный файл', upload_to='main/docs/', blank=False, null=False)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    date_created = models.DateTimeField(verbose_name='Дата создание', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


# Teachers
class Teacher(models.Model):
    full_name = models.CharField(verbose_name='Полная имя', max_length=255)
    branch = models.CharField(verbose_name='Направление', max_length=255, default='')
    image = models.ImageField(verbose_name='Изображение', upload_to='main/authors/', blank=True, null=True)
    about = models.TextField(verbose_name='О педагоге', blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Педагог'
        verbose_name_plural = 'Педагоги'


# News
class News(models.Model):
    title = models.CharField(verbose_name='Название темы', max_length=255)
    poster = models.ImageField(verbose_name='Постер', upload_to='main/news/poster/', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    date_created = models.DateTimeField(verbose_name='Дата создание', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-date_created', )


# Gallery
class Gallery(models.Model):
    title = models.CharField(verbose_name='Название файла', max_length=255)
    file = models.FileField(verbose_name='Исходный файл', upload_to='main/gallery/', blank=False, null=False)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    active = models.BooleanField(verbose_name='Активный', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'




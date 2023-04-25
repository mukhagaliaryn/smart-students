from django.db import models


# Doctype
class Doctype(models.Model):
    doctype_name = models.CharField(verbose_name='Тип документа', max_length=255)

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
    image = models.ImageField(verbose_name='Изображение', upload_to='main/authors/')
    about = models.TextField(verbose_name='О педагоге', blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Педагог'
        verbose_name_plural = 'Педагоги'


# News
class News(models.Model):
    title = models.CharField(verbose_name='Название темы', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


# Gallery
class Gallery(models.Model):
    title = models.CharField(verbose_name='Название файла', max_length=255)
    file = models.FileField(verbose_name='Исходный файл', upload_to='main/gallery/', blank=False, null=False)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'




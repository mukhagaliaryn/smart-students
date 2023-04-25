# Generated by Django 4.2 on 2023-04-25 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_news_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-date_created',), 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='gallery',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Активный'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='branch',
            field=models.CharField(default='', max_length=255, verbose_name='Направление'),
        ),
    ]
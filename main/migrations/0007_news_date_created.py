# Generated by Django 4.2 on 2023-04-25 06:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_news_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создание'),
            preserve_default=False,
        ),
    ]

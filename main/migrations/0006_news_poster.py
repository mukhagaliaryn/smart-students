# Generated by Django 4.2 on 2023-04-25 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_doctype_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='main/news/poster/', verbose_name='Постер'),
        ),
    ]

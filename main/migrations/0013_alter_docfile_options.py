# Generated by Django 4.2 on 2023-11-09 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_docfile_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docfile',
            options={'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
    ]
# Generated by Django 4.2 on 2024-02-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_docfile_options_alter_document_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='is_public',
            field=models.CharField(choices=[('PUBLIC', 'Доступный'), ('PRIVATE', 'Не доступный')], default='Доступный', max_length=255, verbose_name='Тип доступа'),
        ),
    ]

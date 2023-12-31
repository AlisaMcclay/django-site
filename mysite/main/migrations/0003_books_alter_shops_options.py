# Generated by Django 4.1.5 on 2023-01-20 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('author', models.CharField(max_length=60, verbose_name='Автор')),
                ('price', models.CharField(max_length=10, verbose_name='Цена')),
            ],
        ),
        migrations.AlterModelOptions(
            name='shops',
            options={'verbose_name': 'Позиция', 'verbose_name_plural': 'Каталог товаров'},
        ),
    ]

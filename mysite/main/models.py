from django.db import models


class Shops(models.Model):
    title = models.CharField('Название', max_length=50)
    shop = models.TextField('Адрес')
    phone = models.CharField('Телефон', max_length=11, default='88005553535')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Список магазинов'


class Staff(models.Model):
    name = models.CharField('ФИО', max_length=60)
    phone = models.CharField('Телефон', max_length=11)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Список сотрудников'


class Books(models.Model):
    name = models.TextField('Название')
    author = models.CharField('Автор', max_length=60)
    price = models.CharField('Цена', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Каталог товаров'


class Orders(models.Model):
    number = models.CharField('Номер  заказа', max_length=10, default='345')
    bookname = models.TextField('Название книги')
    author = models.CharField('Автор книги', max_length=60)
    client = models.CharField('ФИО покупателя', max_length=60)
    phone = models.CharField('Телефон покупателя', max_length=11)
    shopname = models.CharField('Название магазина', max_length=50)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Журнал заказов'

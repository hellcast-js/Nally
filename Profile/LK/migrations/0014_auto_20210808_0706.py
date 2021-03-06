# Generated by Django 3.2.4 on 2021-08-08 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0013_auto_20210808_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='color',
            field=models.CharField(choices=[('Белый', 'Белый'), ('Желтый', 'Желтый'), ('Зеленый', 'Зеленый'), ('Синий', 'Синий'), ('Красный', 'Красный'), ('Черный', 'Черный')], default='Белый', max_length=40, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='size',
            field=models.CharField(choices=[('100', '100'), ('110', '110'), ('120', '120'), ('130', '130'), ('140', '140'), ('150', '150'), ('160', '160'), ('170', '170'), ('180', '180'), ('190', '190'), ('200', '200'), ('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default='100', max_length=30, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(blank=True, choices=[('Ожидает оплаты', 'Ожидает оплаты'), ('В пути', 'В пути'), ('Доставлено', 'Доставлено')], default='Ожидает оплаты', max_length=20, verbose_name='Статус заказа'),
        ),
    ]

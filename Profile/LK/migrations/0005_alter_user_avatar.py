# Generated by Django 3.2.4 on 2021-08-05 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0004_auto_20210805_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d/', verbose_name='Аватарка'),
        ),
    ]

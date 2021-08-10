# Generated by Django 3.2.4 on 2021-08-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0003_auto_20210805_1957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-id'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='for_all',
            field=models.BooleanField(default=0, verbose_name='Для всех'),
        ),
    ]
# Generated by Django 3.2.4 on 2021-08-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0008_alter_certificates_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='belt',
            field=models.CharField(choices=[('10', '10 гуп'), ('9', '9 гуп'), ('8', '8 гуп'), ('7', '7 гуп'), ('6', '6 гуп'), ('5', '5 гуп'), ('4', '4 гуп'), ('3', '3 гуп'), ('2', '2 гуп'), ('1', '1 гуп'), ('1д', '1 дан'), ('2д', '2 дан'), ('3д', '3 дан'), ('4д', '4 дан'), ('5д', '5 дан'), ('6д', '6 дан'), ('7д', '7 дан'), ('8д', '8 дан'), ('9д', '9 дан')], default='10', max_length=2, verbose_name='Пояс'),
        ),
        migrations.AlterField(
            model_name='trainers',
            name='belt',
            field=models.CharField(choices=[('10', '10 гуп'), ('9', '9 гуп'), ('8', '8 гуп'), ('7', '7 гуп'), ('6', '6 гуп'), ('5', '5 гуп'), ('4', '4 гуп'), ('3', '3 гуп'), ('2', '2 гуп'), ('1', '1 гуп'), ('1д', '1 дан'), ('2д', '2 дан'), ('3д', '3 дан'), ('4д', '4 дан'), ('5д', '5 дан'), ('6д', '6 дан'), ('7д', '7 дан'), ('8д', '8 дан'), ('9д', '9 дан')], default='10', max_length=2, verbose_name='Пояс'),
        ),
    ]
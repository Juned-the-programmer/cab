# Generated by Django 3.1 on 2020-08-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_to',
            field=models.DateField(max_length=50),
        ),
    ]

# Generated by Django 3.1 on 2020-08-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_to',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='from_desti',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='time_to',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_desti',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
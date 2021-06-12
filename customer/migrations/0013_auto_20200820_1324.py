# Generated by Django 3.1 on 2020-08-20 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
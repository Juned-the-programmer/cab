# Generated by Django 3.1 on 2020-08-06 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cname',
        ),
    ]
# Generated by Django 3.1 on 2020-08-19 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20200807_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('c_phone_no', models.IntegerField()),
                ('from_desti', models.CharField(max_length=50)),
                ('to_desti', models.CharField(max_length=50)),
                ('date_to', models.CharField(max_length=50)),
                ('time_to', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-24 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='InwardPayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
            ],
        ),
    ]

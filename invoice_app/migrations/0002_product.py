# Generated by Django 4.2.2 on 2023-07-19 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_cost', models.CharField(max_length=100)),
                ('hsn_no', models.CharField(max_length=100)),
            ],
        ),
    ]
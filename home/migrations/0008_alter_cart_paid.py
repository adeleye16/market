# Generated by Django 4.1.3 on 2022-11-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_cart_options_alter_cart_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]

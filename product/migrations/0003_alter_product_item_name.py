# Generated by Django 4.0.4 on 2022-06-23 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_productsku_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]

# Generated by Django 4.0.4 on 2022-07-07 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_item_name'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='i_product_sku',
        ),
        migrations.RemoveField(
            model_name='location',
            name='l_product_sku',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='t_product_sku',
        ),
        migrations.AddField(
            model_name='inventory',
            name='product_sku',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='product.productsku'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='product_sku',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.productsku'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='product_sku',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='product.productsku'),
            preserve_default=False,
        ),
    ]

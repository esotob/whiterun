# Generated by Django 4.0.4 on 2022-07-07 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_alter_product_item_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('transaction_type', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('transaction_qty', models.IntegerField(default=0)),
                ('reason', models.CharField(max_length=100)),
                ('t_product_sku', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tran_sku_id', to='product.productsku')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinate', models.CharField(max_length=5)),
                ('type', models.CharField(max_length=10)),
                ('location_qty', models.IntegerField(default=0)),
                ('available', models.BooleanField(default=True)),
                ('l_product_sku', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='loc_sku_id', to='product.productsku')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_reserve', models.IntegerField(default=0)),
                ('qty_active', models.IntegerField(default=0)),
                ('qty_allocated', models.IntegerField(default=0)),
                ('qty_packed', models.IntegerField(default=0)),
                ('qty_shipped', models.IntegerField(default=0)),
                ('i_product_sku', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inv_sku_id', to='product.productsku')),
            ],
        ),
    ]

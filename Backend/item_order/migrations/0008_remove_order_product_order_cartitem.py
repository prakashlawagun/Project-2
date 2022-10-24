# Generated by Django 4.0.1 on 2022-10-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcart', '0001_initial'),
        ('item_order', '0007_alter_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='cartitem',
            field=models.ManyToManyField(to='foodcart.CartItems'),
        ),
    ]
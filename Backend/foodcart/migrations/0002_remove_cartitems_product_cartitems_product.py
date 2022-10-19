# Generated by Django 4.0.1 on 2022-10-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_remove_cartitem_cart_remove_cartitem_food_and_more'),
        ('foodcart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='product',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='product',
            field=models.ManyToManyField(to='menu.MenuItem'),
        ),
    ]
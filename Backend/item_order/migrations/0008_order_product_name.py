# Generated by Django 4.0.1 on 2022-10-18 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_order', '0007_delete_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
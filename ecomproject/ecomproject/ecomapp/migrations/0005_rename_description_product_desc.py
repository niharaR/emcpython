# Generated by Django 4.1.5 on 2023-03-18 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_rename_desc_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='desc',
        ),
    ]

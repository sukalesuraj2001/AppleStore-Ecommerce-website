# Generated by Django 4.2 on 2023-05-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_apple_product_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='apple_product',
            name='pimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
    ]
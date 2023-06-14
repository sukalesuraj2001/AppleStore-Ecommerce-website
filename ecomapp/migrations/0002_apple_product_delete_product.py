# Generated by Django 4.2 on 2023-05-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apple_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('cat', models.IntegerField(choices=[(1, 'Iphones'), (2, 'Ipad '), (3, 'Apple Watch'), (4, 'MacBook'), (5, 'MacDesktop'), (6, 'AppleTV'), (7, 'Ipod Touch')], verbose_name='Category')),
                ('price', models.FloatField(verbose_name='Product Price')),
                ('status', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

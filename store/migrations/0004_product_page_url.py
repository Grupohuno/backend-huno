# Generated by Django 4.0.4 on 2022-05-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='page_url',
            field=models.CharField(default='', max_length=180),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1 on 2021-05-26 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210524_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

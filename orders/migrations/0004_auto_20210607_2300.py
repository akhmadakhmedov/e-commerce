# Generated by Django 3.1 on 2021-06-07 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210606_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_line_2',
            field=models.CharField(blank=True, default='exit', max_length=50),
            preserve_default=False,
        ),
    ]

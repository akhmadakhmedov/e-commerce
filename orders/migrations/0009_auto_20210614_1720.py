# Generated by Django 3.1 on 2021-06-14 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20210614_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='payment',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]

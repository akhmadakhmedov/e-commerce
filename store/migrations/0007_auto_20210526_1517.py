# Generated by Django 3.1 on 2021-05-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210526_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cover',
            name='ad_name',
        ),
        migrations.RemoveField(
            model_name='cover',
            name='ad_text',
        ),
        migrations.RemoveField(
            model_name='cover',
            name='image',
        ),
        migrations.AddField(
            model_name='cover',
            name='cover_description',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='cover',
            name='cover_image',
            field=models.ImageField(default=1, upload_to='photos/covers'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cover',
            name='cover_title',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
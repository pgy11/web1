# Generated by Django 3.1.2 on 2021-01-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20210125_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='img',
        ),
        migrations.AddField(
            model_name='book',
            name='image_URL',
            field=models.CharField(default='dd', max_length=200),
            preserve_default=False,
        ),
    ]
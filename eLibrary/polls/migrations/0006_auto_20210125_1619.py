# Generated by Django 3.1.2 on 2021-01-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210125_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.BinaryField(),
        ),
    ]

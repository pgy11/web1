# Generated by Django 3.1.2 on 2021-01-25 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20210125_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='auther',
            new_name='author',
        ),
    ]

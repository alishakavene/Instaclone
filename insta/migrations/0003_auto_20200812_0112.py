# Generated by Django 3.1 on 2020-08-11 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_post_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='name',
        ),
    ]

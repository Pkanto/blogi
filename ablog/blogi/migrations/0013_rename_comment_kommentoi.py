# Generated by Django 4.0.4 on 2022-06-19 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogi', '0012_comment_delete_kommentoi'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Kommentoi',
        ),
    ]

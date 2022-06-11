# Generated by Django 4.0.4 on 2022-06-11 06:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogi', '0004_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blogi_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]

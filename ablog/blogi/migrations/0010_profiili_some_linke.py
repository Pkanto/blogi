# Generated by Django 4.0.4 on 2022-06-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogi', '0009_profiili_profiili_kuva_profiili_some_fb_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiili',
            name='some_linke',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

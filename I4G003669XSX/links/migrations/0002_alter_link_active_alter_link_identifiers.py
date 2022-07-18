# Generated by Django 4.0.5 on 2022-07-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='identifiers',
            field=models.SlugField(blank=True, max_length=20, unique=True),
        ),
    ]

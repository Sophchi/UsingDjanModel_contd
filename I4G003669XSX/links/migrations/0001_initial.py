# Generated by Django 4.0.5 on 2022-07-01 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('target_url', models.URLField()),
                ('description', models.CharField(max_length=200)),
                ('identifiers', models.SlugField(blank=True, max_length=29, unique=True)),
                ('active', models.BooleanField(verbose_name=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

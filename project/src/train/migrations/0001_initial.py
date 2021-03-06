# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-02 02:44
from __future__ import unicode_literals

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
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('data', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Training', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

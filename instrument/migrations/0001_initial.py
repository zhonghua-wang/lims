# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 10:19
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
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('status', models.CharField(choices=[('R', 'ready'), ('O', 'occupied'), ('U', 'unavailable')], default='R', max_length=64)),
                ('image', models.ImageField(max_length=256, upload_to='uploads')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=64, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='instrument',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instrument.User'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo2', models.CharField(max_length=100)),
                ('texto2', models.TextField(max_length=400)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='imagem',
        ),
    ]

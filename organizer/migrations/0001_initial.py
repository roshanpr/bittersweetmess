# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-02 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('pub_date', models.DateField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('founded_date', models.DateField(verbose_name='Date Published')),
                ('contact', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': 'founded_date',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(to='organizer.Tag'),
        ),
        migrations.AddField(
            model_name='newslink',
            name='startup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.Startup'),
        ),
    ]

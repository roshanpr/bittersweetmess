# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-02 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65, unique=True)),
                ('slug', models.SlugField(help_text='Label for URL Configuration', unique_for_month='pub_date')),
                ('text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='date published')),
                ('startups', models.ManyToManyField(related_name='blog_post', to='organizer.Startup')),
                ('tags', models.ManyToManyField(related_name='blog_post', to='organizer.Tag')),
            ],
            options={
                'ordering': ['-pub_date', 'title'],
            },
        ),
    ]

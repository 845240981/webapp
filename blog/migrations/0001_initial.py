# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='标题')),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('body', models.TextField(verbose_name='内容')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布日期')),
                ('created', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', models.CharField(choices=[('draft', '未发布'), ('publish', '发布')], max_length=100, default='draft', verbose_name='状态')),
                ('author', models.ForeignKey(related_name='blog_posts', verbose_name='作者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '帖子',
                'verbose_name_plural': '帖子',
                'ordering': ('-publish',),
            },
        ),
    ]

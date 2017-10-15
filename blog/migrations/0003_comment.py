# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171002_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='用户名', max_length=80)),
                ('email', models.EmailField(verbose_name='邮箱', max_length=254)),
                ('body', models.TextField(verbose_name='内容')),
                ('created', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('active', models.BooleanField(verbose_name='是否被禁', default=True)),
                ('post', models.ForeignKey(to='blog.Post', related_name='comments', verbose_name='所属文章')),
            ],
            options={
                'verbose_name': '评论',
                'ordering': ('created',),
                'verbose_name_plural': '评论',
            },
        ),
    ]

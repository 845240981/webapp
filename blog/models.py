# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  User
from slugify import slugify
from taggit.managers import TaggableManager
from django.core.paginator import  Paginator,EmptyPage,PageNotAnInteger
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='publish')




class Post(models.Model):
    STATUS_CHIOICES =(('draft','未发布'),('publish','发布'))

    title = models.CharField(max_length=250,verbose_name=u'标题')
    slug = models.SlugField(max_length=250,null=True,blank=True)
    tags =  TaggableManager()
    author = models.ForeignKey(User,related_name='blog_posts',verbose_name=u'作者')
    body = models.TextField(verbose_name=u'内容')
    publish = models.DateTimeField(default=timezone.now,verbose_name=u'发布日期')
    created = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
    updated = models.DateTimeField(auto_now=True,verbose_name=u'更新时间')
    status = models.CharField(max_length=100,choices=STATUS_CHIOICES,default='draft',verbose_name=u'状态')
    object = models.Manager()
    published = PublishedManager()



    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save()

    class Meta:
        verbose_name=u'帖子'
        verbose_name_plural=verbose_name
        ordering = ('-publish',)



    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',verbose_name=u'所属文章')
    name = models.CharField(max_length=80,verbose_name=u'用户名')
    email = models.EmailField(verbose_name=u'邮箱')
    body = models.TextField(verbose_name=u'内容')
    created = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
    updated = models.DateTimeField(auto_now=True,verbose_name=u'更新时间')
    active = models.BooleanField(default=True,verbose_name=u'是否被禁')

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name,self.post)



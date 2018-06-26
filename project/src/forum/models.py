# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=u'Тема')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Topic', verbose_name=u'Автор')
    is_archive = models.BooleanField(default=False)
    content = models.TextField(verbose_name=u'Текст')

    class Meta:
        verbose_name = u'Тема'
        verbose_name_plural= u'Темы'
        ordering = 'name', 'id'

    def __str__(self):
        return str(self.name)

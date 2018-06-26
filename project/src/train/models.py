# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings


class Training(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=u'Тип тренировки')
    trainer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Training', verbose_name=u'Руководитель')
    data = models.DateTimeField(verbose_name=u'Дата')
    location = models.CharField(max_length=255, verbose_name=u'Место')

    class Meta:
        verbose_name = u'Тренировка'
        verbose_name_plural= u'Тренировки'
        ordering = 'data', 'id'

    def __str__(self):
        return str(self.name)

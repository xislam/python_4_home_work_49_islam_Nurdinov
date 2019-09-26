from django.db import models


class IssueTracker(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Подробное описание')
    status = models.ForeignKey('Status', related_name='task_status', on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ForeignKey('Type', related_name='task_type', on_delete=models.PROTECT, verbose_name='Тип')
    date_ct = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.summary


class Type(models.Model):
    type = models.CharField(max_length=20, verbose_name='Тип')

    def __str__(self):
        return self.type


class Status(models.Model):
    status = models.CharField(max_length=20, verbose_name='Статус')

    def __str__(self):
        return self.status

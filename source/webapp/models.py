from django.db import models


class IssueTracker(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='кратраткое описание')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='описание')
    status = models.ForeignKey('Status', related_name='issue_status', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')
    type = models.ForeignKey('Type', related_name='issue_type', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Тип')
    Project = models.ForeignKey('Project', related_name='issue_project', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Проект')
    date_ct = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.summary


class Project(models.Model):
    name_pj = models.CharField(max_length=200, null=False, blank=False, verbose_name='имя проекта')
    description_pj = models.TextField(max_length=3000, null=True, blank=True, verbose_name='описание')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now_add=True, verbose_name='Дата изменения')


class Type(models.Model):
    type = models.CharField(max_length=20, verbose_name='Тип')

    def __str__(self):
        return self.type


class Status(models.Model):
    status = models.CharField(max_length=20, verbose_name='Статус')

    def __str__(self):
        return self.status

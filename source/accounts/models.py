from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from django.db.models.signals import post_save
from django.dispatch import receiver
from webapp.models import Project


class Token(models.Model):
    token = models.UUIDField(verbose_name='Token', default=uuid4)
    user = models.ForeignKey('auth.User', related_name='registration_tokens',
                             verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.token)


class Url(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='accounts_url')
    url = models.URLField(max_length=300, null=True, blank=True, verbose_name='Профиль GitHup')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='описание')

    def __str__(self):
        return str(self.url)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Url.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.accounts_url.save()


class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts_user')
    project = models.ForeignKey(Project, related_name='user_project', on_delete=models.PROTECT, null=True,
                                blank=True, verbose_name='Проект')
    created_at = models.DateField(verbose_name='Дата создания')
    finish_at = models.DateField(verbose_name='Дата оканчание', null=True, blank=True)


    def __str__(self):
        return str(self.user)



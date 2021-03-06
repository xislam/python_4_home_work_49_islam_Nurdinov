# Generated by Django 2.2 on 2019-11-05 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20191105_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuetracker',
            name='created_by',
            field=models.ForeignKey(default=webapp.models.get_admin, on_delete=django.db.models.deletion.PROTECT, related_name='issue', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]

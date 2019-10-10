# Generated by Django 2.2 on 2019-10-10 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuetracker',
            name='Project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='issue_project', to='webapp.Project', verbose_name='Проект'),
        ),
        migrations.AlterField(
            model_name='issuetracker',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='issue_status', to='webapp.Status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='issuetracker',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='issue_type', to='webapp.Type', verbose_name='Тип'),
        ),
    ]

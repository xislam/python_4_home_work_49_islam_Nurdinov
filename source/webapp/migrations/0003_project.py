# Generated by Django 2.2 on 2019-10-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20191004_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pj', models.CharField(max_length=200, verbose_name='имя проекта')),
                ('description_pj', models.TextField(blank=True, max_length=3000, null=True, verbose_name='описание')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(auto_now_add=True, verbose_name='Дата изменения')),
            ],
        ),
    ]

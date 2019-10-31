# Generated by Django 2.2 on 2019-10-31 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=300, verbose_name='Профиль GitHup')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accounts_url', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

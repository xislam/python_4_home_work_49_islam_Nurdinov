# Generated by Django 2.2 on 2019-11-02 12:26

from django.db import migrations


class Migration(migrations.Migration):

    def get_initial_for_field(self, field, field_name):
        if field_name in self.Meta.profile_fields:
            return getattr(self.instance.profile, field_name)

        return super().get_initial_for_field(field, field_name)

    dependencies = [
        ('accounts', '0003_auto_20191102_0926'),
    ]

    operations = [
    ]

# Generated by Django 2.2.12 on 2020-04-28 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecos', '0007_auto_20200423_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasource',
            old_name='datasource_name',
            new_name='name',
        ),
    ]
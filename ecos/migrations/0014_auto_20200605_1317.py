# Generated by Django 2.2.12 on 2020-06-05 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecos', '0013_ecossite_ecoss'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ecossite',
            old_name='ecoss',
            new_name='is_ecoss',
        ),
    ]
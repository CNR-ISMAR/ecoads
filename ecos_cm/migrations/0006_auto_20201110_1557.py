# Generated by Django 2.2.13 on 2020-11-10 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecos_cm', '0005_auto_20201110_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cmpage',
            old_name='model_hi',
            new_name='model_human_interactions',
        ),
    ]

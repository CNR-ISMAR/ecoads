# Generated by Django 3.1.7 on 2021-05-21 14:54

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecos', '0037_auto_20210521_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inforesource',
            name='info_resource_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Monitoring program', 'Monitoring program'), ('Portal', 'Portal'), ('Map', 'Map'), ('Dataset', 'Dataset'), ('Other', 'Other')], max_length=43),
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-21 10:38

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecos', '0036_auto_20210517_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inforesource',
            name='info_resource_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Monitoring program', 'Monitoring program'), ('Portal', 'Portal'), ('Geospatial layer', 'Geospatial layer'), ('Dataset', 'Dataset'), ('Other', 'Other')], max_length=56),
        ),
    ]

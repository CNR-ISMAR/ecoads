# Generated by Django 3.1.7 on 2021-04-27 12:50

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecos', '0029_auto_20210427_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=400)),
                ('info_resource_type', models.CharField(choices=[('Monitoring program', 'Monitoring program'), ('Portal', 'Portal'), ('Geospatial layer', 'Geospatial layer')], default='Monitoring program', max_length=100)),
                ('description', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('reference_url', models.URLField(max_length=600, null=True)),
                ('reference_institution', models.TextField(blank=True, null=True)),
                ('additional_informations', wagtail.core.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]

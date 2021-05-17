# Generated by Django 3.1.7 on 2021-05-17 15:39

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecos', '0035_auto_20210513_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inforesource',
            name='reference_url',
        ),
        migrations.AlterField(
            model_name='inforesource',
            name='reference_institution',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]
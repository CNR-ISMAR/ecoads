# Generated by Django 2.2.13 on 2020-11-10 15:43

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecos_cm', '0003_cmpage_model_hi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmpage',
            name='model_hi',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]

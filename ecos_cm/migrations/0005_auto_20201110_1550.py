# Generated by Django 2.2.13 on 2020-11-10 15:50

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecos_cm', '0004_auto_20201110_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmpage',
            name='model_ep',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cmpage',
            name='model_ov',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cmpage',
            name='model_pi',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]

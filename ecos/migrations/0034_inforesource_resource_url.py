# Generated by Django 3.1.7 on 2021-05-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecos', '0033_auto_20210504_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='inforesource',
            name='resource_url',
            field=models.URLField(max_length=600, null=True),
        ),
    ]

# Generated by Django 2.2.13 on 2020-11-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecos', '0018_auto_20201005_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecossite',
            name='img',
            field=models.URLField(max_length=600, null=True),
        ),
    ]

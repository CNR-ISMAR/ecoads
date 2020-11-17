# Generated by Django 2.2.13 on 2020-11-17 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecos_cm', '0009_remove_cmpage_ecossite'),
        ('ecos', '0019_ecossite_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecossite',
            name='conceptualmodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecos_cm.CMPage'),
        ),
    ]

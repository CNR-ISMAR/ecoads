# Generated by Django 3.1.7 on 2021-05-04 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecos', '0031_inforesource_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='EcosSitesInfoResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecos_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecos.ecossite')),
                ('inforesources', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecos.inforesource')),
            ],
        ),
        migrations.AddField(
            model_name='ecossite',
            name='inforesources',
            field=models.ManyToManyField(blank=True, through='ecos.EcosSitesInfoResource', to='ecos.InfoResource'),
        ),
    ]

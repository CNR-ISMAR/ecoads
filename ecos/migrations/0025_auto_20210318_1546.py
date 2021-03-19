# Generated by Django 2.2.13 on 2021-03-18 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0014_auto_20210318_1535'),
        ('ecos', '0024_auto_20210318_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='EcosSitesLocationDjangoMeasurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecos_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecos.EcosSite')),
                ('measurement_locationid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurements.Location')),
            ],
        ),
        migrations.AddField(
            model_name='ecossite',
            name='measurement_location_id',
            field=models.ManyToManyField(through='ecos.EcosSitesLocationDjangoMeasurements', to='measurements.Location'),
        ),
    ]

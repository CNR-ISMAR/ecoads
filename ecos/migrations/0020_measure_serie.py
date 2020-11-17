# Generated by Django 2.2.13 on 2020-11-12 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecos', '0019_ecossite_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField(blank=True, null=True)),
                ('data_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecos.DataSource')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecos.Parameter')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(db_index=True)),
                ('value', models.FloatField()),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecos.Serie')),
            ],
            options={
                'unique_together': {('serie', 'timestamp', 'value')},
            },
        ),
    ]
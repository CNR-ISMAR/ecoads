# Generated by Django 2.2.13 on 2020-08-03 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecos', '0016_ecossite_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='EcosSitesParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecos_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecos.EcosSite')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecos.Parameter')),
            ],
        ),
        migrations.AddField(
            model_name='ecossite',
            name='parameters',
            field=models.ManyToManyField(through='ecos.EcosSitesParameters', to='ecos.Parameter'),
        ),
    ]
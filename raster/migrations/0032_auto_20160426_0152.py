# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raster', '0031_auto_20160218_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legendentry',
            name='expression',
            field=models.CharField(help_text='Use a number or a valid numpy logical expression where x is thepixel value. For instance: "(-3.0 < x) & (x <= 1)" or "x <= 1".', max_length=500),
        ),
        migrations.AlterField(
            model_name='rasterlayer',
            name='datatype',
            field=models.CharField(choices=[('co', 'Continuous'), ('ca', 'Categorical'), ('ma', 'Mask'), ('ro', 'Rank Ordered')], default='co', max_length=2),
        ),
        migrations.AlterField(
            model_name='rasterlayer',
            name='max_zoom',
            field=models.IntegerField(blank=True, help_text='Leave blank to automatically determine the max zoom level from the raster scale. Otherwise the raster parsed up to the zoom level specified here.', null=True),
        ),
        migrations.AlterField(
            model_name='rasterlayer',
            name='nodata',
            field=models.CharField(blank=True, help_text='Leave blank to keep the internal band nodata values. If a nodata value is specified here, it will be used for all bands of this raster.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rasterlayer',
            name='rasterfile',
            field=models.FileField(blank=True, null=True, upload_to='rasters'),
        ),
        migrations.AlterField(
            model_name='rasterlayer',
            name='srid',
            field=models.IntegerField(blank=True, help_text='Leave blank to use the internal raster srid. If a srid is specified here, it will be used for all calculations.', null=True),
        ),
        migrations.AlterField(
            model_name='rasterlayerparsestatus',
            name='log',
            field=models.TextField(default='', editable=False),
        ),
        migrations.AlterField(
            model_name='rasterlayerparsestatus',
            name='status',
            field=models.IntegerField(choices=[(0, 'Layer not yet parsed'), (1, 'Downloading file'), (2, 'Reprojecting'), (3, 'Creating tiles'), (4, 'Dropping empty tiles'), (5, 'Finished parsing'), (6, 'Failed parsing')], default=0),
        ),
        migrations.AlterField(
            model_name='rasterlayerreprojected',
            name='rasterfile',
            field=models.FileField(blank=True, null=True, upload_to='rasters/reprojected'),
        ),
    ]

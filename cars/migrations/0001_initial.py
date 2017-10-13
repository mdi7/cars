# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('make', models.CharField(default=0, max_length=20)),
                ('model_num', models.CharField(default=0, max_length=30)),
                ('year', models.IntegerField(default=0)),
                ('cartype', models.CharField(default=0, max_length=20)),
                ('fuel_type', models.CharField(default=0, max_length=20)),
                ('Gas_Milage', models.CharField(default=0, max_length=20)),
                ('PRICE', models.FloatField(default=0)),
                ('image', models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'pic_folder/')),
            ],
        ),
    ]

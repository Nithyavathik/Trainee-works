# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('serialno', models.IntegerField()),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=30)),
                ('phonenumber', models.IntegerField(max_length=10)),
                ('emailId', models.CharField(max_length=100)),
            ],
        ),
    ]

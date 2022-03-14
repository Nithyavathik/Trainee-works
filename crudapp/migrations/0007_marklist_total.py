# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0006_auto_20220302_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='marklist',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]

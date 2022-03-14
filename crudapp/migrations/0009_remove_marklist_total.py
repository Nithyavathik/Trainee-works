# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0008_auto_20220302_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marklist',
            name='total',
        ),
    ]

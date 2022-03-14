# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0009_remove_marklist_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marklist',
            name='StId',
            field=models.ForeignKey(to='crudapp.Student'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0007_marklist_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marklist',
            name='StId',
            field=models.ForeignKey(related_name='Students', to='crudapp.Student'),
        ),
    ]

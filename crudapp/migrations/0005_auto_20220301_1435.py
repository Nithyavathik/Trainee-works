# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0004_auto_20220301_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarks',
            name='StuId',
            field=models.ForeignKey(related_name='Studentname', to='crudapp.Student'),
        ),
        migrations.AlterField(
            model_name='studentmarks',
            name='SubjectName',
            field=models.CharField(max_length=50),
        ),
    ]

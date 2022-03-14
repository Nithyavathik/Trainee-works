# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_studentmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarks',
            name='StuId',
            field=models.ForeignKey(to='crudapp.Student'),
        ),
        migrations.AlterField(
            model_name='studentmarks',
            name='SubjectName',
            field=models.ForeignKey(related_name='StudentName', to='crudapp.Student'),
        ),
    ]

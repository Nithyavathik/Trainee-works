# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_auto_20220215_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMarks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('SubjectName', models.CharField(max_length=50)),
                ('SubjectMark', models.IntegerField()),
                ('StuId', models.ForeignKey(related_name='studentId', to='crudapp.Student')),
            ],
        ),
    ]

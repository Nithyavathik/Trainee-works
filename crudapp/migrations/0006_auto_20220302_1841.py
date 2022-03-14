# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0005_auto_20220301_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marklist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Language', models.IntegerField()),
                ('Maths', models.IntegerField()),
                ('Physics', models.IntegerField()),
                ('Chemistry', models.IntegerField()),
                ('Biology', models.IntegerField()),
                ('StId', models.ForeignKey(related_name='Studentname', to='crudapp.StudentMarks')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='emailId',
            field=models.EmailField(max_length=100),
        ),
    ]

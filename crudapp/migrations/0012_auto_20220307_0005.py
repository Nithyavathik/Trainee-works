# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0011_auto_20220305_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marklist',
            options={'verbose_name_plural': 'Marklists'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'students'},
        ),
        migrations.AlterModelOptions(
            name='studentmarks',
            options={'verbose_name_plural': 'Studentmarks'},
        ),
        migrations.AlterModelTable(
            name='marklist',
            table='marklists',
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
        migrations.AlterModelTable(
            name='studentmarks',
            table='studentmarks',
        ),
    ]

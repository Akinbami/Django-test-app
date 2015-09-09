# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20150901_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='matric_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

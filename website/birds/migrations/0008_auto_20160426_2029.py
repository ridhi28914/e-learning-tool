# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160322152221 on 2016-04-26 20:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0007_choicegramm_quesgramm'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quesgramm',
            new_name='Questiongramm',
        ),
    ]

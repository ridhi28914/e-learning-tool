# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160322152221 on 2016-05-01 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0009_auto_20160426_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionmaths',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Choicegramm',
            new_name='Choicemaths',
        ),
        migrations.DeleteModel(
            name='Questiongramm',
        ),
        migrations.RemoveField(
            model_name='question',
            name='group',
        ),
        migrations.AlterField(
            model_name='choicemaths',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birds.Questionmaths'),
        ),
    ]

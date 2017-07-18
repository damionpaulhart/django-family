# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_auto_20170715_2312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['lastName', 'firstName', 'middleNames', '-birth__date']},
        ),
        migrations.AddField(
            model_name='person',
            name='orderHelper',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='marriage',
            name='album',
            field=models.ManyToManyField(blank=True, null=True, to='family.Photograph'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthFirstName',
            field=models.CharField(blank=True, help_text='(if different)', max_length=30, verbose_name='Birth First Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthName',
            field=models.CharField(blank=True, max_length=30, verbose_name='Maiden/Birth Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='firstName',
            field=models.CharField(blank=True, max_length=20, verbose_name='First/Given Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastName',
            field=models.CharField(max_length=30, verbose_name='Last/Family Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='middleNames',
            field=models.CharField(blank=True, max_length=50, verbose_name='Middle Names(s)'),
        ),
        migrations.AlterField(
            model_name='person',
            name='nickName',
            field=models.CharField(blank=True, max_length=20, verbose_name='Nickname'),
        ),
    ]
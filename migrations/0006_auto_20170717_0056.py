# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0005_auto_20170716_0150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marriage',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='person',
            name='orderHelper',
        ),
        migrations.AlterField(
            model_name='marriage',
            name='spouses',
            field=models.ManyToManyField(related_name='marriages', to='family.Person'),
        ),
    ]

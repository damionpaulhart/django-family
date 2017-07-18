# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 22:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import family.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country_code', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='documents')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventType', models.PositiveSmallIntegerField(choices=[(0, 'Birth'), (2, 'Death'), (3, 'Burial')])),
                ('date', family.fields.UncertainDateField()),
                ('reference', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Place Name', max_length=30)),
                ('city', models.CharField(blank=True, help_text='City / Town / Village', max_length=30)),
                ('county_state_province', models.CharField(blank=True, help_text='County / State / Province', max_length=30, verbose_name='county/state/province')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('country', models.ForeignKey(help_text='Country', on_delete=django.db.models.deletion.CASCADE, to='family.Country')),
            ],
            options={
                'ordering': ['country', 'county_state_province', 'city', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Marriage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', family.fields.UncertainDateField(blank=True, null=True)),
                ('reference', models.URLField(blank=True, null=True)),
                ('divorced', family.fields.UncertainDateField(blank=True, null=True)),
                ('isMarriage', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=None, max_length=1)),
                ('bio', tinymce.models.HTMLField(blank=True)),
                ('firstName', models.CharField(blank=True, help_text='First/Given Name', max_length=20)),
                ('middleNames', models.CharField(blank=True, help_text='Middle Names(s)', max_length=50)),
                ('nickName', models.CharField(blank=True, help_text='Nickname', max_length=20)),
                ('lastName', models.CharField(help_text='Last/Family Name', max_length=30)),
                ('birthName', models.CharField(blank=True, help_text='Maiden/Birth Name', max_length=30)),
                ('birthFirstName', models.CharField(blank=True, help_text='Birth First Name (if different)', max_length=30)),
                ('birth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='family.Event')),
                ('burial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='family.Event')),
                ('death', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='family.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('caption', models.TextField(blank=True)),
                ('date', family.fields.UncertainDateField(blank=True, null=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='family.Location')),
                ('people', models.ManyToManyField(related_name='photos', to='family.Person')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='person',
            name='mugshot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo_of', to='family.Photograph'),
        ),
        migrations.AddField(
            model_name='person',
            name='parents',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children_of', to='family.Marriage'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='marriage',
            name='album',
            field=models.ManyToManyField(to='family.Photograph'),
        ),
        migrations.AddField(
            model_name='marriage',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weddings', to='family.Location'),
        ),
        migrations.AddField(
            model_name='marriage',
            name='spouses',
            field=models.ManyToManyField(to='family.Person'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='family.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='family.Person'),
        ),
        migrations.AddField(
            model_name='document',
            name='people',
            field=models.ManyToManyField(related_name='documents', to='family.Person'),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('country', 'county_state_province', 'city', 'name')]),
        ),
    ]
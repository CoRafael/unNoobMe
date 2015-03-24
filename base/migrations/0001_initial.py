# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('duration', models.IntegerField()),
                ('type_of_meeting', models.CharField(max_length=150)),
                ('date', models.DateTimeField()),
                ('lesson', models.CharField(max_length=150)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'Computer Science', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accepted', models.BooleanField(default=False)),
                ('advertisement', models.ForeignKey(to='base.Advertisement')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.IntegerField(default=0)),
                ('comment', models.CharField(default=b'', max_length=250)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(default=b'Glasgow', max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('picture', models.ImageField(upload_to=b'avatar_pictures', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userInterest', models.ManyToManyField(to='base.Interest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rating',
            name='author',
            field=models.ForeignKey(to='base.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rating',
            name='offer',
            field=models.ForeignKey(to='base.JobOffer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='joboffer',
            name='user',
            field=models.ForeignKey(to='base.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='advInterest',
            field=models.ForeignKey(to='base.Interest'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(to='base.UserProfile'),
            preserve_default=True,
        ),
    ]

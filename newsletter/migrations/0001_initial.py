# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=200, verbose_name=b'Enter your E-mail')),
                ('full_name', models.CharField(max_length=200, null=True, verbose_name=b'Enter your Full name', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'Updated at')),
            ],
        ),
    ]

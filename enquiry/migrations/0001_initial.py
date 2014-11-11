# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('eid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=75)),
                ('subject', models.CharField(max_length=200)),
                ('desc', models.TextField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-02 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_remove_questionnaire_succesful_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='succesful_applicant',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-02 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOpenings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('pretext', models.TextField(max_length=300)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MBA', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Do you have an MBA?')),
                ('Formal_Training', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Do you have formal training in finance')),
                ('Description', models.TextField(blank=True, default='', max_length=250, null=True, verbose_name='Describe the trainings you have acquired')),
                ('Employment_Status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='Are you currently employed')),
                ('Employment_Fields', models.CharField(choices=[('Investment Banking - 5 years and above', 'Investment Banking - 5 years and above'), ('Mergers and Acquisitions and Stock Trading - 5 years and above', 'Mergers and Acquisitions and Stock Trading - 5 years and above'), ('Previous CFO Position - 3 years and above', 'Previous CFO Position - 3 years and above'), ('Previous CEO Position - 3 years and above', 'Previous CEO Position - 3 years and above'), ('Senior level Auditor - 3 years and above', 'Senior level Auditor - 3 years and above')], max_length=200, verbose_name='Select any of the following fields that represent your experience')),
                ('Equity', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Do you care about having equity?')),
                ('Salary_for_equity', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Are you willing to trade a portion of salary for equity? ')),
                ('Job_Salary', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='Can you live on N250,000 or less for the next 9 months?')),
                ('Job_Time', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='I just want a 9-5 job to pay the bills')),
                ('Told_What_to_do', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='I like to be told what to do')),
                ('Entrepreneur', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='I am an entrepreneur at heart')),
                ('Dislikes', models.CharField(choices=[('Igbos', 'Igbos'), ('Yorubas', 'Yorubas'), ('Northerners', 'Northerners'), ('Southerners', 'Southerners'), ('None', 'None')], max_length=100, verbose_name='Who do you dislike the most?')),
                ('Get_along_with', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('All', 'All')], max_length=100, verbose_name='Who do you get along with')),
                ('Gay_people', models.CharField(choices=[('Definitely', 'Definitely'), ('Not at all', 'Not at all'), ('Indifferent', 'Indifferent')], max_length=100, verbose_name='Gay people are disgusting and should be put in jail')),
                ('Muslims', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='I cannot stand muslims')),
                ('Christians', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='Christians and others are infidels')),
                ('succesful_applicant', models.BooleanField(default=False)),
                ('job_opening', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.JobOpenings')),
            ],
        ),
        migrations.CreateModel(
            name='Rsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MBA', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Do you have an MBA?')),
                ('Formal_Training', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=250, verbose_name='Do you have formal training in Business development')),
                ('Description', models.TextField(blank=True, default='', max_length=250, null=True, verbose_name='Describe the trainings you have acquired')),
                ('Employment_Status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=250, verbose_name='Are you currently employed')),
                ('Employment_Fields', models.CharField(choices=[('Software Sales - 5 years and above', 'Software Sales - 5 years and above'), ('Software Business Development - 5 years and above', 'Software Business Development - 5 years and above')], max_length=200, verbose_name='Select any of the following fields that represent your experience')),
                ('Client_acquisition', models.TextField(verbose_name='Tell us how you intend to approach client acquisition')),
                ('Client_retention', models.TextField(verbose_name='Tell us how you intend to approach client retention')),
                ('Equity', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Do you care about having equity?')),
                ('Salary_for_equity', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Are you willing to trade a portion of salary for equity? ')),
                ('Job_Salary', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Can you live on N250,000 or less for the next 3-6 months?')),
                ('Job_Time', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='I just want a 9-5 job to pay the bills')),
                ('Told_What_to_do', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='I like to be told what to do')),
                ('Entrepreneur', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='I am an entrepreneur at heart')),
                ('Dislikes', models.CharField(choices=[('Igbos', 'Igbos'), ('Yorubas', 'Yorubas'), ('Northerners', 'Northerners'), ('Southerners', 'Southerners'), ('None', 'None')], max_length=100, verbose_name='Who do you dislike the most?')),
                ('Get_along_with', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('All', 'All')], max_length=100, verbose_name='Who do you get along with')),
                ('Gay_people', models.CharField(choices=[('Definitely', 'Definitely'), ('Not at all', 'Not at all'), ('Indifferent', 'Indifferent')], max_length=100, verbose_name='Gay people are disgusting and should be put in jail')),
                ('Muslims', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='I cannot stand muslims')),
                ('Christians', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='Christians and others are infidels')),
                ('succesful_applicant', models.BooleanField(default=False)),
                ('job_opening', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.JobOpenings')),
            ],
        ),
    ]

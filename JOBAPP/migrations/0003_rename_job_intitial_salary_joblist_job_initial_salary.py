# Generated by Django 5.0.6 on 2024-05-16 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JOBAPP', '0002_joblist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joblist',
            old_name='job_intitial_salary',
            new_name='job_initial_salary',
        ),
    ]

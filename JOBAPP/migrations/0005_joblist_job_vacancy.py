# Generated by Django 5.0.6 on 2024-05-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JOBAPP', '0004_joblist_job_application_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='job_vacancy',
            field=models.IntegerField(null=True),
        ),
    ]

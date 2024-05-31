# Generated by Django 5.0.6 on 2024-05-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JOBAPP', '0003_rename_job_intitial_salary_joblist_job_initial_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='job_application_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='joblist',
            name='job_company_description',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='joblist',
            name='job_company_email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='joblist',
            name='job_company_phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='joblist',
            name='job_description',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='joblist',
            name='job_education',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='joblist',
            name='job_experience',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='joblist',
            name='job_skills',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
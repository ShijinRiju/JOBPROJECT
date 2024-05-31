from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class CustomLogin(AbstractUser):
    userType = models.CharField(max_length = 100)
    viewPass = models.CharField(max_length = 100)
    
class Register(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.IntegerField()
    login_id = models.ForeignKey(CustomLogin,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    
class JobList(models.Model):
    job_title = models.CharField(max_length = 100)
    job_company = models.CharField(max_length = 100)
    job_location = models.CharField(max_length = 100)
    job_initial_salary = models.IntegerField()
    job_final_salary = models.IntegerField()
    job_type = models.CharField(max_length = 100)
    job_company_description = models.CharField(max_length = 3000, null=True)
    job_description = models.CharField(max_length = 3000, null=True)
    job_skills = models.CharField(max_length = 3000, null=True)
    job_education = models.CharField(max_length = 3000, null=True)
    job_experience = models.CharField(max_length = 3000, null=True)
    job_company_email = models.EmailField(max_length = 100, null=True)
    job_company_phone = models.IntegerField(null=True)
    job_application_date = models.DateField(null=True)
    job_vacancy = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.job_title
    
    def time_since_posted(self):
        now = timezone.now()
        time_difference = now - self.timestamp
        
        if time_difference.days > 0:
            return f"{time_difference.days} {'day' if time_difference.days == 1 else 'days'} ago"
        elif time_difference.seconds >= 3600:
            hours = time_difference.seconds // 3600
            return f"{hours} {'hour' if hours == 1 else 'hours'} ago"
        elif time_difference.seconds >= 60:
            minutes = time_difference.seconds // 60
            return f"{minutes} {'minute' if minutes == 1 else 'minutes'} ago"
        else:
            return "Just Now"
        
class Application(models.Model):
    user_id = models.ForeignKey(Register, on_delete=models.CASCADE)
    job_id = models.ForeignKey(JobList,on_delete=models.CASCADE)
    applicant_education = models.CharField(max_length=100)
    applicant_experience = models.CharField(max_length=100)
    applicant_internship = models.CharField(max_length=3000)
    applicant_cv = models.FileField()
    applied_status = models.CharField(max_length = 100, default="Not Applied", null = True) 
    status = models.CharField(max_length = 100, default="Pending", null=True)
    
    def __str__(self):
        return self.user_id.name
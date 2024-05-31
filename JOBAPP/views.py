from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import *
from .forms import JobSearchForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.POST:
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        name = f"{first_name} {last_name}"
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm']
        
        if not CustomLogin.objects.filter(email = email).exists():
            if password == confirm_password:
                login_query = CustomLogin.objects.create_user(username = email,password = password,userType = "USER",viewPass = password)
                login_query.save()
                register_query = Register.objects.create(name = name,email = email,phone = phone,login_id = login_query)
                register_query.save()
                return redirect('/signin')
            else:
                return HttpResponse('<script>alert("Password doesnot match");window.location.href="/register"</script>')
        else:
            return HttpResponse('<script>alert("Email already exists");window.location.href="/register"</script>')
    return render(request, 'register.html')

def signin(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = email, password = password)
        
        if user is not None:
            if not user.check_password(password):
                return HttpResponse('<script>alert("Wrong Password");window.location.href="/signin"</script>')
            else:
                login(request,user)
                if user.userType == "USER":
                    request.session['user_id'] = user.id
                    return redirect('/user_index')
                elif user.userType == "ADMIN":
                    request.session['admin_id'] = user.id
                    return redirect('/admin_index')
        else:
            return HttpResponse('<script>alert("Invalid email or password");window.location.href="/signin"</script>')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    request.session.flush()
    return redirect('/signin')
    

def user_index(request):
    user = request.session['user_id']
    return render(request, 'user_index.html')

def job_listing(request):
    user = request.session.get('user_id')
    query = request.GET.get('search-bar')
    
    if query:
        job_list = JobList.objects.filter(
            Q(job_title__icontains=query) |
            Q(job_company__icontains=query) |
            Q(job_location__icontains=query) |
            Q(job_description__icontains=query) |
            Q(job_skills__icontains=query)
        )
    else:
        job_list = JobList.objects.all()

    row_count = job_list.count()
    
    jobs_with_application_status = []
    for job in job_list:
        has_applied = Application.objects.filter(user_id__login_id=user, job_id=job).exists()
        jobs_with_application_status.append({
            'job': job,
            'has_applied': has_applied
        })
    
    p = Paginator(jobs_with_application_status, 3)
    page = request.GET.get('page')
    pagination = p.get_page(page)
    
    return render(request, 'job_listing.html', {
        "count": row_count,
        "pagination": pagination,
        "query": query,
    })
    
def admin_index(request):
    user = request.session['admin_id']
    return render(request, 'admin_index.html')

def job_publish(request):
    user_id = request.session['admin_id']
    if request.POST:
        job_title = request.POST['job_title']
        job_description = request.POST['description']
        job_location = request.POST['job_location']
        skills = request.POST['skills']
        education = request.POST['education']
        experience = request.POST['experience']
        company_description = request.POST['company_description']
        company_name = request.POST['company_name']
        company_email = request.POST['company_email']
        company_phone = request.POST['company_phone']
        application_date = request.POST['application_date']
        initial_salary = request.POST['initial_salary']
        final_salary = request.POST['final_salary']
        job_type = request.POST['job_type']
        job_vacancy = request.POST['job_vacancy']
        create_query = JobList.objects.create(
            job_title = job_title,
            job_location = job_location,
            job_company = company_name,
            job_initial_salary = initial_salary,
            job_final_salary = final_salary,
            job_type = job_type,
            job_company_description = company_description,
            job_description = job_description,
            job_skills = skills,
            job_education = education,
            job_experience = experience,
            job_company_email = company_email,
            job_company_phone = company_phone,
            job_application_date = application_date,
            job_vacancy = job_vacancy,
            )
        create_query.save()
        
    return render(request, 'job_publish.html')

def job_details(request):
    user = request.session['user_id']
    id = request.GET['id']
    data = JobList.objects.get(id=id)
    job_list = JobList.objects.all()
    salary = data.job_final_salary
    total_salary = int(salary)*12
    has_applied = Application.objects.filter(user_id__login_id=user, job_id=data).exists()
        
    return render(request, 'job_details.html',{"data":data,"total_salary":total_salary,"has_applied":has_applied})

def job_apply(request):
    user_id = request.session['user_id']
    id = request.GET['id']
    data = JobList.objects.get(id=id)
    user = Register.objects.get(login_id = user_id)
    
    if request.POST:
        applicant_education = request.POST['applicant_education']
        applicant_experience = request.POST['applicant_experience']
        applicant_internship = request.POST['applicant_internship']
        applicant_cv = request.FILES['applicant_cv']
        application_query = Application.objects.create(
            user_id = user,
            job_id = data,
            applicant_education = applicant_education,
            applicant_experience = applicant_experience,
            applicant_internship = applicant_internship,
            applicant_cv = applicant_cv,
            applied_status = "Applied"
            )
        application_query.save()
        return redirect('/job_listing')
    
    return render(request, 'job_apply.html',{"data":data,"user":user})

def my_jobs(request):
    user_id = request.session['user_id']
    data = Application.objects.filter(user_id__login_id = user_id)
    return render(request, 'my_jobs.html', {"data":data})

def applicant_details(request):
    user_id = request.session['admin_id']
    datas = Application.objects.filter(status = "Pending")
    approved_data = Application.objects.filter(status = "Approved")
    rejected_data = Application.objects.filter(status = "Rejected")
    return render(request, 'applicant_details.html',{"data":datas,"approved_data":approved_data,"rejected_data":rejected_data})

def applications(request):
    user_id = request.session['admin_id']
    id = request.GET['id']
    application_data = Application.objects.get(user_id__login_id = id,status = "Pending")
    return render(request, 'applications.html',{"data":application_data})

def approve_application(request):
    id = request.GET['id']
    update_query = Application.objects.filter(id=id).update(status="Approved")
    return redirect('/admin_index')

def reject_application(request):
    id = request.GET['id']
    update_query = Application.objects.filter(id=id).update(status="Rejected")
    return redirect('/admin_index')
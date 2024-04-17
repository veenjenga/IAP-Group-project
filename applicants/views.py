
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from .models import *

@csrf_exempt
def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not all([username, email, password]):
            return JsonResponse({'error': 'All fields are required.'}, status=400)
        
        try:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Create the corresponding UserProfile with user_id2
            user_profile = UserProfile.objects.create(user=user, is_admin=False)
            user_profile.save()  # Ensure user_id2 is generated and saved
            
            return JsonResponse({
                'message': 'User created successfully.',
                'user_id2': user_profile.user_id2
            }, status=201)
        
        except IntegrityError:
            return JsonResponse({'error': 'Username already exists.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)



from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login as auth_login


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not all([username, password]):
            return JsonResponse({'error': 'Both username and password are required.'}, status=400)
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                user_profile = UserProfile.objects.get(user=user)
                request.session['user_id2'] = user_profile.user_id2
                request.session.set_expiry(1800)  # Session expires in 30 minutes
                return JsonResponse({'message': 'Login successful.', 'is_admin': user_profile.is_admin,
                                     'is_authenticated': True, 'user_id2': user_profile.user_id2}, status=200)
            except UserProfile.DoesNotExist:
                return JsonResponse({'error': 'UserProfile does not exist.'}, status=400)
        else:
            return JsonResponse({'error': 'Invalid username or password.'}, status=400)



from django.views.decorators.http import require_http_methods
from .forms import JobForm
from django.contrib.auth.decorators import login_required

@csrf_exempt
@require_http_methods(["POST"])
def create_job(request):
    user_id2 = request.session.get('user_id2')
    if not user_id2:
        return JsonResponse({'error': 'User not logged in or session expired'}, status=403)

    title = request.POST.get('title')
    description = request.POST.get('description')
    
    if not all([title, description]):
        return JsonResponse({'error': 'Missing title or description'}, status=400)

    try:
        user_profile = UserProfile.objects.get(user_id2=user_id2)
        job = Job(title=title, description=description, posted_by=user_profile)
        job.save()
        return JsonResponse({'message': 'Job created successfully'}, status=201)
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'UserProfile not found'}, status=404)

import re

from django.db.models import Q

@require_http_methods(["GET"])
def search_jobs(request):
    keyword = request.GET.get('keyword', '')
    if keyword:
        # Use a simple pattern directly in the query
        jobs = Job.objects.filter(description__iregex=keyword)
    else:
        jobs = Job.objects.all()
    
    jobs_data = [{'id': job.id, 'title': job.title, 'description': job.description} for job in jobs]
    return JsonResponse({'jobs': jobs_data}, safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def submit_application(request):
    try:
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')
        job_id = request.POST.get('job_id')
        user_id2 = request.session.get('user_id2')

        print("Received data:", cover_letter, job_id, user_id2)  # Log received data
        if resume:
            print("Resume filename:", resume.name)

        if not all([cover_letter, resume, job_id, user_id2]):
            return JsonResponse({'error': 'All fields are required. Ensure the cover letter and resume are included.'}, status=400)

        job = Job.objects.get(id=job_id)
        applicant = UserProfile.objects.get(user_id2=user_id2)
        application = Application(job=job, applicant=applicant, cover_letter=cover_letter, resume=resume)
        application.save()
        return JsonResponse({'message': 'Application submitted successfully'}, status=201)
    except Job.DoesNotExist:
        return JsonResponse({'error': 'Job not found'}, status=404)
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'User profile not found'}, status=404)
    except Exception as e:
        print(e)  # Log any other exception
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def user_applications(request):
    user_id2 = request.session.get('user_id2')
    applications = Application.objects.filter(
        applicant__user_id2=user_id2
    ).select_related('job', 'applicationstatus')  # Corrected to use select_related

    return render(request, 'applicants/user_applications.html', {
        'applications': applications
    })




@csrf_exempt
def show_signup(request):
    return render(request, 'applicants/signup.html')

@csrf_exempt
def show_login(request):
    return render(request, 'applicants/login.html')

@csrf_exempt
def show_home(request):
    return render(request, 'applicants/home.html')

@csrf_exempt
def show_admin(request):
    return render(request, 'applicants/admin.html')

@csrf_exempt
def show_user(request):
    return render(request, 'applicants/user.html')

@csrf_exempt
def create_job_template(request):
    return render(request, 'applicants/createjob.html')

@csrf_exempt
def apply(request):
    return render(request, 'applicants/apply.html')
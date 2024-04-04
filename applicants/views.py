
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
            
            # Create the corresponding UserProfile
            UserProfile.objects.create(user=user, is_admin=False)
            
            return JsonResponse({'message': 'User created successfully.'}, status=201)
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
                is_admin = user_profile.is_admin
            except UserProfile.DoesNotExist:
                is_admin = False
            
            return JsonResponse({'message': 'Login successful.', 'is_admin': is_admin}, status=200)
        else:
            return JsonResponse({'error': 'Invalid username or password.'}, status=400)



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
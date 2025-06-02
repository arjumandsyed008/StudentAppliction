from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, StudentProfileForm, ApplicationForm
from .models import Application, Course, StudentProfile
from django.contrib.auth import login, authenticate,logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to some page after login
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout






def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('dashboard')
    else:
        user_form = UserRegisterForm()
        profile_form = StudentProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def dashboard(request):
    profile = StudentProfile.objects.get(user=request.user)
    applications = Application.objects.filter(student=profile)
    return render(request, 'dashboard.html', {'applications': applications})

@login_required
def apply_course(request):
    profile = StudentProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.student = profile
            app.save()
            return redirect('dashboard')
    else:
        form = ApplicationForm()
    return render(request, 'apply_course.html', {'form': form})
